from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from database.queries import *

member_view = Blueprint("member_view", __name__)


@member_view.route("/member/dashboard")
def member_dashboard():
    member_id = session.get("member_id") 
    username = session.get("username")
    raw_exercises = get_member_exercises(member_id)
    exercises = [f"{i+1}) {name} - {date}" for i, (_, _, name, date) in enumerate(raw_exercises)]
    raw_achievements = get_member_achievements(member_id)
    achievements = raw_achievements[0][0].split(",")
    raw_health_stats = get_member_health_stats(member_id)
    health_stats = {
        "Weight": f"{raw_health_stats[0][2]}lbs",
        "Heart Rate": f"{raw_health_stats[0][3]}bpm",
        "Average Hours of Sleep": raw_health_stats[0][4],
    }
    return render_template("member/member_dashboard.html", member=username, exercises=exercises, achievements=achievements, health_stats=health_stats)


@member_view.route("/member/profile", methods=["GET", "POST"])
def member_profile():
    if request.method == "POST":
        flash("Profile updated successfully", "success")
        return redirect(url_for("member_view.member_dashboard"))
    else:
        member = get_member_by_id(session.get("member_id"))
        raw_exercises = get_member_exercises(session.get("member_id"))
        exercises = [exercise[2] for exercise in raw_exercises]
        raw_health_stats = get_member_health_stats(session.get("member_id"))
        health_stats = [raw_health_stats[0][2], raw_health_stats[0][3], raw_health_stats[0][4]]
        return render_template("member/member_profile.html", member=member, exercises=exercises, health_stats=health_stats)
    

@member_view.route("/member/schedule", methods=["GET", "POST"])
def member_schedule():
    if request.method == "POST":
        trainer_id = request.form.get("trainer_id")
        session_time = request.form.get("session_time")
        member_id = session.get("member_id")  # Assuming you're storing the member id in session
        book_session(member_id, trainer_id, session_time)
        flash("Session booked successfully", "success")
        return redirect(url_for("member_view.member_dashboard"))
    else:
        trainers = get_available_trainers()
        return render_template("member/member_schedule.html", trainers=trainers)
    

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

        update_user_profile(user_type, username, password, fitness_goal, achievements)
        update_member_health_stats(member_id, weight, heart_rate, sleep)
        update_member_exercises(member_id, exercises)
        flash("Profile updated successfully.", "success")
        return redirect(url_for("member_view.member_dashboard"))


@member_view.route("/bookSession", methods=["POST"])
def book_session():
    if request.method == "POST":
        username = session["username"]
        trainer_id = request.form.get("trainer_id")
        session_time = request.form.get("session_time")
        session_type = request.form.get("session_type")

        book_new_session(username, trainer_id, session_time, session_type)
        flash("Session booked successfully.", "success")
        return redirect(url_for("member_view.member_schedule"))