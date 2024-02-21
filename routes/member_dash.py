from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from database.queries import *

member_dash = Blueprint("member_dash", __name__)

@member_dash.route("/member/dashboard")
def member_dashboard():
    member_id = session.get("member_id") 
    member = get_member_by_id(member_id)
    exercises = get_member_exercises(member_id)
    achievements = get_member_achievements(member_id)
    health_stats = get_member_health_stats(member_id)
    return render_template("member/member_dashboard.html", member=member, exercises=exercises, achievements=achievements, health_stats=health_stats)


@member_dash.route("/member/profile", methods=["GET", "POST"])
def member_profile():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        fitness_goal = request.form.get("fitness_goal")
        health_metrics = request.form.get("health_metrics")
        member_id = session.get("member_id")  # Assuming you're storing the member id in session
        update_member(member_id, username, password, fitness_goal, health_metrics)
        flash("Profile updated successfully")
        return redirect(url_for("member_dash.member_dashboard"))
    else:
        member = get_member_by_id(session.get("member_id"))
        return render_template("member/member_profile.html", member=member)
    

@member_dash.route("/member/schedule", methods=["GET", "POST"])
def member_schedule():
    if request.method == "POST":
        trainer_id = request.form.get("trainer_id")
        session_time = request.form.get("session_time")
        member_id = session.get("member_id")  # Assuming you're storing the member id in session
        book_session(member_id, trainer_id, session_time)
        flash("Session booked successfully")
        return redirect(url_for("member_dash.member_dashboard"))
    else:
        trainers = get_available_trainers()
        return render_template("member/member_schedule.html", trainers=trainers)
    

@member_dash.route("/updateProfile", methods=["POST"])
def update_profile():
    if request.method == "POST":
        username = session["username"]
        user_type = session["user_type"]
        fitness_goal = request.form.get("fitness_goal")
        health_metrics = request.form.get("health_metrics")
        exercises = request.form.get("exercises")
        statistics = request.form.get("statistics")
        achievements = request.form.get("achievements")

        update_user_profile(user_type, username, fitness_goal, health_metrics, exercises, statistics, achievements)
        flash("Profile updated successfully.")
        return redirect(url_for("member_dash.member_dashboard"))