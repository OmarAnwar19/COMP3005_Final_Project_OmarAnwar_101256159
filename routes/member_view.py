from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from util.helpers import format_datetime, validate_password
from database.queries.trainer_queries import get_available_trainers, get_trainer_availability
from database.queries.admin_queries import get_available_rooms
from database.queries.session_queries import book_new_session, make_session_payment, cancel_member_session
from database.queries.member_queries import *

member_view = Blueprint("member_view", __name__)


@member_view.route("/member/dashboard")
def member_dashboard():
    member_id = session.get("member_id") 
    username = session.get("username")
    raw_sessions = get_member_sessions(member_id)
    sessions = [
        f"{i+1}) {s_type} with {trainer} in {room} - {format_datetime(date)}" 
        for i, (_, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    raw_exercises = get_member_exercises(member_id)
    exercises = [
        f"{i+1}) {name} - {format_datetime(date)}" 
        for i, (_, _, name, date) in enumerate(raw_exercises)
    ]
    raw_achievements = get_member_achievements(member_id)
    achievements = raw_achievements[0][0].split(",")
    raw_health_stats = get_member_health_stats(member_id)
    health_stats = {
        "Weight": f"{raw_health_stats[0][2]}lbs",
        "Heart Rate": f"{raw_health_stats[0][3]}bpm",
        "Avg. Nightly Sleep": f"{raw_health_stats[0][4]}hrs",
    }
    return render_template("member/member_dashboard.html", member=username, sessions=sessions, exercises=exercises, achievements=achievements, health_stats=health_stats)


@member_view.route("/member/profile")
def member_profile():
    member = get_member_by_id(session.get("member_id"))
    raw_exercises = get_member_exercises(session.get("member_id"))
    exercises = [exercise[2] for exercise in raw_exercises]
    raw_health_stats = get_member_health_stats(session.get("member_id"))
    health_stats = [raw_health_stats[0][2], raw_health_stats[0][3], raw_health_stats[0][4]]
    return render_template("member/member_profile.html", member=member, exercises=exercises, health_stats=health_stats)
    

@member_view.route("/updateProfile", methods=["POST"])
def update_profile():
    if request.method == "POST":
        user_type = session["user_type"]
        member_id = session["member_id"]
        username = request.form.get("username")
        password = request.form.get("password")
        fitness_goal = request.form.get("fitness_goal")
        exercises = request.form.getlist("exercises")
        achievements = request.form.get("achievements")
        weight = request.form.get("weight")
        heart_rate = request.form.get("heart_rate")
        sleep = request.form.get("sleep")

        user = get_member_by_username(user_type, username)
        if user:
            flash(f"{user_type} {username} already exists.", "warning")
        elif not validate_password(password):
            flash("Password must be at least 6 characters long, and contain a number and an uppercase letter.", "danger")
        else:
            update_member_profile(user_type, username, password, fitness_goal, achievements)
            update_member_health_stats(member_id, weight, heart_rate, sleep)
            update_member_exercises(member_id, exercises)
            flash("Profile updated successfully!", "success")
            return redirect(url_for("member_view.member_dashboard"))
        return redirect(url_for("member_view.member_profile"))


@member_view.route("/member/schedule")
def member_schedule():
    member_id = session.get("member_id") 
    raw_sessions = get_member_sessions(member_id)
    sessions = [{
        "id": id, 
        "info": f"{i+1}) {s_type} with {trainer} in {room} - {format_datetime(date)}"
        } for i, (id, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    trainers = get_available_trainers()
    rooms = get_available_rooms()
    return render_template("member/member_schedule.html", trainers=trainers, sessions=sessions, rooms=rooms)


@member_view.route("/member/bookSession", methods=["POST"])
def book_session():
    if request.method == "POST":
        member_id = session.get("member_id")
        trainer_id = request.form.get("trainer_id")
        room_id = request.form.get("room_id")
        session_time = datetime.strptime(request.form.get("session_time"), "%Y-%m-%dT%H:%M").time()
        session_type = request.form.get("session_type")

        available_from, available_to = get_trainer_availability(trainer_id)[0]

        if not (available_from <= session_time <= available_to):
            flash("Trainer is not available at that time.", "danger")
            return redirect(url_for("member_view.member_schedule"))

        session_id = book_new_session(member_id, trainer_id, room_id, session_time, session_type)
        flash("Session booked successfully!", "success")
        make_session_payment(member_id, session_id, 120 if session_type == "Personal Training" else 90)
        flash("Payment pending processing.", "info")

        return redirect(url_for("member_view.member_dashboard"))
    

@member_view.route("/member/cancelSession", methods=["POST"])
def cancel_session():
    if request.method == "POST":
        session_id = request.form.get("session_id")
        cancel_member_session(session_id)
        flash("Session cancelled successfully!", "success")
        return redirect(url_for("member_view.member_schedule"))