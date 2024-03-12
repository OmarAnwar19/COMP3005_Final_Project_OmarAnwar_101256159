from flask import render_template, Blueprint, session, request, redirect, url_for, flash
# importing all the queries from the database.queries package that we need for the admin view
from database.queries.admin_queries import *
# importing the format_date, format_datetime, and format_datetime_for_html functions from the util.helpers package
from util.helpers import format_date, format_datetime, format_datetime_for_html

# creating a blueprint for the admin view
admin_view = Blueprint("admin_view", __name__)


# creating a route for the admin dashboard
@admin_view.route("/admin/dashboard")
def admin_dashboard():
    # getting the admin username from the session
    username = session.get("username")
    users = get_all_users()
    # get the members and trainers from the users list and format them into a list of strings
    members = [username for username, role in users if role == 'Member']
    trainers = [username for username, role in users if role == 'Trainer']
    # get the raw equipment from the database and format it into a list of dictionaries
    raw_equipment = get_all_equipment()
    equipment = [{
        "id": id, 
        "name": name,
        "broken": broken,
        "maintenance_date": format_date(date)
        } for (id, name, broken, date) in (raw_equipment)
    ]
    # get the raw sessions from the database and format them into a list of strings
    raw_sessions = get_admin_sessions()
    sessions = [
        f"{i+1}) {s_type}, {member_name} with {trainer_name} in {room_name} - {format_datetime(date)}" 
        for i, (_, _, _, _, date, s_type, member_name, trainer_name, room_name) in enumerate(raw_sessions)
    ]
    # render the admin dashboard with the username, sessions, members, trainers, and equipment
    return render_template("admin/admin_dashboard.html", admin=username, sessions=sessions, members=members, trainers=trainers, equipment=equipment)


# creating a route for the manage rooms page
@admin_view.route("/admin/manage/rooms")
def manage_rooms():
    # get the room bookings from the database and format them into a list of dictionaries
    bookings = get_room_bookings()
    bookings = [{
        "id": id, 
        "name": room_name,
        "booked": bool(booked),
        # for the user name, session time, session type, and trainer name, we need to check if they are None
        # if they are, we set the value to 'N/A' just as a placeholder
        "user_name": member if member is not None else 'N/A',
        "session_time": format_datetime(date) if date is not None else 'N/A',
        "session_type": s_type if s_type is not None else 'N/A',
        "trainer_name": trainer if trainer is not None else 'N/A',
        } for (_, id, room_name, booked, date, s_type, member, trainer) in bookings
    ]
    # render the manage rooms page with the room bookings
    return render_template("admin/manage_rooms.html", rooms=bookings)


# creating a route for the manage schedule page
@admin_view.route("/admin/manage/schedule")
def manage_schedule():
    # get the room bookings from the database and format them into a list of dictionaries
    bookings = get_room_bookings()
    bookings = [{
        "id": id, 
        "name": room_name,
        # same as above, set any missing values to placeholders
        "user_name": member if member is not None else 'N/A',
        "session_time": format_datetime_for_html(date) if date is not None else 'N/A',
        "session_type": s_type if s_type is not None else 'N/A',
        "trainer_name": trainer if trainer is not None else 'N/A',
        } for (id, _, room_name, booked, date, s_type, member, trainer) in bookings if booked
    ]
    # render the manage schedule page with the room bookings
    return render_template("admin/manage_schedule.html", rooms=bookings)


# creating a route for the manage payments page
@admin_view.route("/admin/manage/payments")
def manage_payments():
    # get the payments from the database and format them into a list of dictionaries
    raw_payments = get_all_payments()
    payments = [{
        "id": id, 
        "payment_date": format_datetime(date),
        "amount": amount,
        "processed": bool(processed),
        "approved": bool(approved),
        "member_name": member,
        "trainer_name": trainer,
        "session_type": s_type
        } for (id, _, _, amount, date, processed, approved, member, trainer, s_type) in raw_payments
    ]
    # separate the payments into unprocessed, approved, and rejected by filtering the payments based on the processed and approved keys
    unprocessed = [p for p in payments if not p["processed"]]
    approved = [p for p in payments if p["processed"] and p["approved"]]
    rejected = [p for p in payments if p["processed"] and not p["approved"]]
    # render the manage payments page with the payments
    return render_template("admin/manage_payments.html", unprocessed_payments=unprocessed, approved_payments=approved, rejected_payments=rejected)


# creating a route for the manage equipment page
@admin_view.route("/admin/callMaintenance", methods=["POST"])
def call_maintenance():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the equipment id from the form
        equipment_id = request.form.get("equipment_id")
        # call the fix_equipment function with the equipment id
        fix_equipment(equipment_id)
        # flash a message and redirect to the admin dashboard
        flash("Maintenance called. Equipment will be fixed soon.", "info")
        return redirect(url_for("admin_view.admin_dashboard"))


# creating a route for the manage equipment page
@admin_view.route("/admin/changeMaintenanceDate", methods=["POST"])
def change_maintenance_date():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the equipment id and new date from the form
        equipment_id = request.form.get("equipment_id")
        new_date = request.form.get("maintenance_date")
        # call the update_equipment_maintenance_date function with the equipment id and new date
        update_equipment_maintenance_date(equipment_id, new_date)
        # flash a message and redirect to the admin dashboard
        flash("Maintenance date updated.", "info")
        return redirect(url_for("admin_view.admin_dashboard"))
    

# creating a route for the manage equipment page
@admin_view.route("/admin/addRoom", methods=["POST"])
def add_room():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the room name from the form
        room_name = request.form.get("room_name")
        # call the add_room function with the room name
        add_room(room_name)
        # flash a message and redirect to the admin dashboard
        flash("Room added successfully!", "success")
        return redirect(url_for("admin_view.admin_dashboard"))
    

@admin_view.route("/admin/unbookRoom", methods=["POST"])
def unbook_room_session():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the room id from the form
        room_id = request.form.get("room_id")
        # call the unbook_room function with the room id
        unbook_room(room_id)
        # flash a message and redirect to the admin dashboard
        flash("Room unbooked successfully!", "success")
        return redirect(url_for("admin_view.manage_rooms"))


# creating a route for the manage equipment page
@admin_view.route("/admin/deleteRoom", methods=["POST"])
def delete_room_session():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the room id from the form
        room_id = request.form.get("room_id")
        # call the delete_room function with the room id
        delete_room(room_id)
        # flash a message and redirect to the admin dashboard
        flash("Room deleted successfully!", "success")
        return redirect(url_for("admin_view.manage_rooms"))


# creating a route for the manage equipment page
@admin_view.route("/admin/updateSessionTime", methods=["POST"])
def update_room_session_time():
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # get the session id and new time from the form
        session_id = request.form.get("session_id")
        new_time = request.form.get("new_time")
        # call the update_session_time function with the session id and new time
        update_session_time(session_id, new_time)
        # flash a message and redirect to the admin dashboard
        flash("Session time updated successfully!", "success")
        return redirect(url_for("admin_view.manage_schedule"))


# creating a route for the manage equipment page
@admin_view.route('/admin/approvePayment/<int:payment_id>', methods=['POST'])
def handle_approve_payment(payment_id):
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # call the approve_payment function with the payment id
        approve_payment(payment_id)
        # flash a message and redirect to the admin dashboard
        flash("Payment approved successfully!", "success")
        return redirect(url_for("admin_view.manage_payments"))


# creating a route for the manage equipment page
@admin_view.route('/admin/rejectPayment/<int:payment_id>', methods=['POST'])
def handle_reject_payment(payment_id):
    # making sure the request method is POST, so that we dont get any errors
    if request.method == "POST":
        # call the reject_payment function with the payment id
        reject_payment(payment_id)
        flash("Payment rejected successfully!", "success")
        return redirect(url_for("admin_view.manage_payments"))