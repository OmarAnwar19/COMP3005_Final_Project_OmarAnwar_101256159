from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for, flash, session
# importing all the queries from the database.queries package that we need for the member view
from database.queries.trainer_queries import get_available_trainers, get_trainer_availability
from database.queries.admin_queries import get_available_rooms, get_room_name
from database.queries.trainer_queries import get_trainer_username
from database.queries.session_queries import book_new_session, make_session_payment, cancel_member_session
from database.queries.member_queries import *
# importing the format_datetime function from the util.helpers package
from util.helpers import format_datetime, validate_password

member_view = Blueprint("member_view", __name__)


# creating a route for the member dashboard
@member_view.route("/member/dashboard")
def member_dashboard():
    # getting the member id and username from the session
    member_id = session.get("member_id") 
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


# creating a route for the member profile
@member_view.route("/member/profile")
def member_profile():
    # get the member id, username, exercises, and health stats from the session
    member = get_member_by_id(session.get("member_id"))
    raw_exercises = get_member_exercises(session.get("member_id"))
    # format the exercises into a list of strings
    exercises = [exercise[2] for exercise in raw_exercises]
    raw_health_stats = get_member_health_stats(session.get("member_id"))
    # format the health stats into a list of strings
    health_stats = [raw_health_stats[0][2], raw_health_stats[0][3], raw_health_stats[0][4]]
    # render the member profile page with the member, exercises, and health stats
    return render_template("member/member_profile.html", member=member, exercises=exercises, health_stats=health_stats)


# creating a route for the member schedule
@member_view.route("/member/schedule")
def member_schedule():
    # get the member id from the session
    member_id = session.get("member_id") 
    # get the member sessions, available trainers, and available rooms from the database
    raw_sessions = get_member_sessions(member_id)
    trainers = get_available_trainers()
    rooms = get_available_rooms()
    # format the sessions into a list of strings
    sessions = [{
        "id": id, 
        "info": f"{i+1}) {s_type} with {trainer} in {room} - {format_datetime(date)}"
        } for i, (id, _, _, _, date, s_type, trainer, room) in enumerate(raw_sessions)
    ]
    # render the member schedule page with the available trainers, sessions, and rooms
    return render_template("member/member_schedule.html", trainers=trainers, sessions=sessions, rooms=rooms)


# creating a route for the member checkout
@member_view.route("/member/checkout", methods=['GET', 'POST'])
def member_checkout():
    # get the sessions from the session
    sessions = session.get('cart', [])
    # render the member checkout page with the sessions
    return render_template("member/member_checkout.html", sessions=sessions)


# creating a POST route for the member to update their profile
@member_view.route("/member/updateProfile", methods=["POST"])
def update_profile():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get all the form data from the request
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

        # get the member by username their username
        user = get_member_by_username(user_type, username)
        # if the member exists, flash a warning message
        if user:
            flash(f"{user_type} {username} already exists.", "warning")
        # or if the password is invalid, flash a danger message
        elif not validate_password(password):
            flash("Password must be at least 6 characters long, and contain a number and an uppercase letter.", "danger")
        # otherwise, update the member profile, health stats, and exercises
        else:
            # update the member profile, health stats, and exercises with the appropriate queries
            update_member_profile(user_type, username, password, fitness_goal, achievements)
            update_member_health_stats(member_id, weight, heart_rate, sleep)
            update_member_exercises(member_id, exercises)
            # flash a success message and redirect to the member profile page
            flash("Profile updated successfully!", "success")
            return redirect(url_for("member_view.member_dashboard"))
        # if there are any errors, redirect to the member profile page
        return redirect(url_for("member_view.member_profile"))


# creating a POST route for the member to cancel a session
@member_view.route("/member/cancelSession", methods=["POST"])
def cancel_session():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the session id from the form
        session_id = request.form.get("session_id")
        # cancel the member session with the appropriate query
        cancel_member_session(session_id)
        # flash a success message and redirect to the member schedule page
        flash("Session cancelled successfully!", "success")
        return redirect(url_for("member_view.member_schedule"))
    

# creating a POST route for the member to add a booking to their cart
@member_view.route('/member/addToCart', methods=['POST'])
def add_to_cart():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the member id, trainer id, room id, session time, and session type from the form
        member_id = session.get("member_id")
        trainer_id = request.form.get("trainer_id")
        room_id = request.form.get("room_id")
        # convert the session time to a datetime object using the format_datetime function
        session_datetime = datetime.strptime(request.form.get("session_time"), "%Y-%m-%dT%H:%M")
        session_type = request.form.get("session_type")

        # check if the trainer is available at the session time
        available_from, available_to = get_trainer_availability(trainer_id)[0]
        # if the session time is not within the trainer's availability, flash a danger message and redirect to the member schedule page
        if not (available_from <= session_datetime.time() <= available_to):
            flash("Trainer is not available at that time.", "danger")
            return redirect(url_for("member_view.member_schedule"))
        
        # create a booking dictionary with the member id, trainer id, room id, session time, and session type
        booking = {
            "id": len(session['cart']) + 1 if 'cart' in session else 1,
            "member_id": member_id,
            "trainer_id": trainer_id,
            "amount": 120 if session_type == "Personal Training" else 90,
            "room_id": room_id,
            "session_time": session_datetime, 
            "session_type": session_type,
            "info": f"{session_type} with {get_trainer_username(trainer_id)} in {get_room_name(room_id)} - {format_datetime(session_datetime)}" 
        }

        # if there is no cart in the session, create a new cart
        if 'cart' not in session:
            session['cart'] = []
        # append the booking to the cart
        session['cart'].append(booking)

        # flash a success message and redirect to the member schedule page
        flash("Booking added to cart successfully!", "success")
        return redirect(url_for("member_view.member_schedule"))
    

# creating a POST route for the member to remove a booking from their cart
@member_view.route('/member/removeFromCart', methods=['POST'])
def remove_from_cart():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the booking id from the form
        booking_id = request.form.get("booking_id")
        # remove the booking from the cart with the given booking id
        session['cart'] = [booking for booking in session['cart'] if booking['id'] != int(booking_id)]
        # flash a success message and redirect to the checkout page if the request came from the checkout page or the schedule page otherwise
        flash("Booking removed from cart successfully!", "success")
        if 'checkout' in request.referrer:
            return redirect(url_for("member_view.member_checkout"))
        return redirect(url_for("member_view.member_schedule"))
    

# creating a POST route for the member to confirm their payment
@member_view.route("/member/confirmCheckout", methods=["POST"])
def confirm_payment():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the cart from the session
        cart = session.get("cart")
        # loop through the bookings in the cart and book 
        for booking in cart:
            # get the member id, trainer id, room id, session time, and session type from the booking
            member_id = booking["member_id"]
            trainer_id = booking["trainer_id"]
            room_id = booking["room_id"]
            session_time = booking["session_time"]
            session_type = booking["session_type"]
            # book the new session and make the session payment with the appropriate queries
            session_id = book_new_session(member_id, trainer_id, room_id, session_time, session_type)
            make_session_payment(member_id, session_id, booking["amount"])
        # clear the cart from the session
        session.pop("cart", None)
        # flash a success message and redirect to the member dashboard
        flash("Sessions booked successfully! Thank you!", "success")
        # flash a message that the payment is pending processing and redirect to the member dashboard
        flash("Payment pending processing.", "info")
        return redirect(url_for("member_view.member_dashboard"))