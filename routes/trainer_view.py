from flask import render_template, Blueprint, session, request, redirect, url_for, flash
from database.queries.trainer_queries import *
from database.queries.member_queries import get_member_sessions, get_member_exercises, get_member_achievements, get_member_health_stats, get_member_username
from util.helpers import format_date

trainer_view = Blueprint("trainer_view", __name__)


@trainer_view.route("/trainer/dashboard")
def trainer_dashboard():
    trainer_id = session.get("member_id") 
    username = session.get("username")
    availability = get_trainer_availability(trainer_id)[0]
    raw_sessions = get_trainer_sessions(trainer_id)
    sessions = [
        f"{i+1}) {s_type} with {trainer} in {room} - {format_date(date)}" 
        for i, (_, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    return render_template("trainer/trainer_dashboard.html", trainer=username, sessions=sessions, availability=availability)


@trainer_view.route("/trainer/search")
def member_search():
    return render_template("trainer/search/member_search.html")


@trainer_view.route("/trainer/search/member/<int:member_id>")
def member_details(member_id):
    username = get_member_username(member_id)
    raw_sessions = get_member_sessions(member_id)
    sessions = [
        f"{i+1}) {s_type} with {trainer} in {room} - {format_date(date)}" 
        for i, (_, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    raw_exercises = get_member_exercises(member_id)
    exercises = [
        f"{i+1}) {name} - {format_date(date)}" 
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
    return render_template("trainer/search/member_page.html", member=username, sessions=sessions, exercises=exercises, achievements=achievements, health_stats=health_stats)


@trainer_view.route("/trainer/updateSchedule", methods=["POST"])
def update_schedule():
    if request.method == "POST":
        trainer_id = session["member_id"]
        available_from = request.form.get("available_from")
        available_to = request.form.get("available_to")
        flash("Availability updated successfully!", "success")
        update_trainer_availability(trainer_id, available_from, available_to)
        return redirect(url_for("trainer_view.trainer_dashboard"))
    

@trainer_view.route("/trainer/searchMembers", methods=["POST"])
def member_search_results():
    if request.method == "POST":
        search_query = request.form.get("search_query")
        members = search_members(search_query)
        return render_template("trainer/search/member_search.html", members=members)