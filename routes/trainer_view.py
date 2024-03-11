from flask import render_template, Blueprint, session, request, redirect, url_for, flash
# importing all the queries from the database.queries package that we need for the trainer view
from database.queries.trainer_queries import *
from database.queries.member_queries import get_member_sessions, get_member_exercises, get_member_achievements, get_member_health_stats, get_member_username
from util.helpers import format_datetime

# creating a blueprint for the trainer view
trainer_view = Blueprint("trainer_view", __name__)


# creating a route for the trainer dashboard
@trainer_view.route("/trainer/dashboard")
def trainer_dashboard():
    # getting the trainer id and username from the session
    trainer_id = session.get("member_id") 
    username = session.get("username")
    # getting the trainer availability,
    availability = get_trainer_availability(trainer_id)[0]
    # get the raw sessions from the database, and format them into a list of strings
    raw_sessions = get_trainer_sessions(trainer_id)
    sessions = [
        f"{i+1}) {s_type} with {trainer} in {room} - {format_datetime(date)}" 
        for i, (_, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    # render the trainer dashboard with the username, sessions, and availability
    return render_template("trainer/trainer_dashboard.html", trainer=username, sessions=sessions, availability=availability)


# creating a route for the trainer schedule
@trainer_view.route("/trainer/search")
def member_search():
    return render_template("trainer/search/member_search.html")


# creating a route for the search results of a member
@trainer_view.route("/trainer/search/member/<int:member_id>")
def member_details(member_id):
    # get the member username, sessions, exercises, achievements, and health stats from the database
    username = get_member_username(member_id)
    raw_sessions = get_member_sessions(member_id)
    # format the sessions into a list of strings
    sessions = [
        f"{i+1}) {s_type} with {trainer} in {room} - {format_datetime(date)}" 
        for i, (_, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    raw_exercises = get_member_exercises(member_id)
    # format the exercises into a list of strings
    exercises = [
        f"{i+1}) {name} - {format_datetime(date)}" 
        for i, (_, _, name, date) in enumerate(raw_exercises)
    ]
    # for the achievements, we need to split the string into a list
    raw_achievements = get_member_achievements(member_id)
    achievements = raw_achievements[0][0].split(",")
    # get the health stats and format them into a dictionary of strings
    raw_health_stats = get_member_health_stats(member_id)
    health_stats = {
        "Weight": f"{raw_health_stats[0][2]}lbs",
        "Heart Rate": f"{raw_health_stats[0][3]}bpm",
        "Avg. Nightly Sleep": f"{raw_health_stats[0][4]}hrs",
    }
    # render the member page with the member username, sessions, exercises, achievements, and health stats
    return render_template("trainer/search/member_page.html", member=username, sessions=sessions, exercises=exercises, achievements=achievements, health_stats=health_stats)


# creating a POST route for the trainer to update their availability
@trainer_view.route("/trainer/updateSchedule", methods=["POST"])
def update_schedule():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # getting the trainer id from the session, and the availability from the form
        trainer_id = session["member_id"]
        available_from = request.form.get("available_from")
        available_to = request.form.get("available_to")
        # updating the trainer availability in the database
        update_trainer_availability(trainer_id, available_from, available_to)
        # redirecting the trainer to their dashboard, and flashing a success message
        flash("Availability updated successfully!", "success")
        return redirect(url_for("trainer_view.trainer_dashboard"))
    

# creating a POST route for the trainer to add a session
@trainer_view.route("/trainer/searchMembers", methods=["POST"])
def member_search_results():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # getting the search query from the form, and searching for members with that query
        search_query = request.form.get("search_query")
        members = search_members(search_query)
        # rendering the member search page with the search results
        return render_template("trainer/search/member_search.html", members=members)