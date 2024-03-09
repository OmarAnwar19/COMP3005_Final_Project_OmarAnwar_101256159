from flask import render_template, Blueprint, session, request, redirect, url_for, flash
from database.queries.admin_queries import *
from util.helpers import format_date, format_datetime, format_datetime_for_html

admin_view = Blueprint("admin_view", __name__)


@admin_view.route("/admin/dashboard")
def admin_dashboard():
    username = session.get("username")
    users = get_all_users()
    members = [username for username, role in users if role == 'Member']
    trainers = [username for username, role in users if role == 'Trainer']
    raw_equipment = get_all_equipment()
    equipment = [{
        "id": id, 
        "name": name,
        "broken": broken,
        "maintenance_date": format_date(date)
        } for (id, name, broken, date) in (raw_equipment)
    ]
    raw_sessions = get_admin_sessions()
    sessions = [
        f"{i+1}) {s_type}, {member_name} with {trainer_name} in {room_name} - {format_datetime(date)}" 
        for i, (_, _, _, _, date, s_type, member_name, trainer_name, room_name) in enumerate(raw_sessions)
    ]
    return render_template("admin/admin_dashboard.html", admin=username, sessions=sessions, members=members, trainers=trainers, equipment=equipment)


@admin_view.route("/admin/manage/rooms")
def manage_rooms():
    bookings = get_room_bookings()
    bookings = [{
        "id": id, 
        "name": room_name,
        "booked": bool(booked),
        "user_name": member if member is not None else 'N/A',
        "session_time": format_datetime(date) if date is not None else 'N/A',
        "session_type": s_type if s_type is not None else 'N/A',
        "trainer_name": trainer if trainer is not None else 'N/A',
        } for (_, id, room_name, booked, date, s_type, member, trainer) in bookings
    ]
    return render_template("admin/manage_rooms.html", rooms=bookings)


@admin_view.route("/admin/manage/schedule")
def manage_schedule():
    bookings = get_room_bookings()
    bookings = [{
        "id": id, 
        "name": room_name,
        "user_name": member if member is not None else 'N/A',
        "session_time": format_datetime_for_html(date) if date is not None else 'N/A',
        "session_type": s_type if s_type is not None else 'N/A',
        "trainer_name": trainer if trainer is not None else 'N/A',
        } for (id, _, room_name, booked, date, s_type, member, trainer) in bookings if booked
    ]
    return render_template("admin/manage_schedule.html", rooms=bookings)


@admin_view.route("/admin/manage/payments")
def manage_payments():
    return render_template("admin/manage_payments.html")


@admin_view.route("/admin/callMaintenance", methods=["POST"])
def call_maintenance():
    if request.method == "POST":
        equipment_id = request.form.get("equipment_id")
        fix_equipment(equipment_id)
        flash("Maintenance called. Equipment will be fixed soon.", "info")
        return redirect(url_for("admin_view.admin_dashboard"))


@admin_view.route("/admin/changeMaintenanceDate", methods=["POST"])
def change_maintenance_date():
    if request.method == "POST":
        equipment_id = request.form.get("equipment_id")
        new_date = request.form.get("maintenance_date")
        update_equipment_maintenance_date(equipment_id, new_date)
        flash("Maintenance date updated.", "info")
        return redirect(url_for("admin_view.admin_dashboard"))
    

@admin_view.route("/admin/addRoom", methods=["POST"])
def add_room():
    if request.method == "POST":
        room_name = request.form.get("room_name")
        add_room(room_name)
        flash("Room added successfully!", "success")
        return redirect(url_for("admin_view.admin_dashboard"))
    

@admin_view.route("/admin/deleteRoom", methods=["POST"])
def delete_room_session():
    if request.method == "POST":
        room_id = request.form.get("room_id")
        delete_room(room_id)
        flash("Room deleted successfully!", "success")
        return redirect(url_for("admin_view.manage_rooms"))


@admin_view.route("/admin/updateSessionTime", methods=["POST"])
def update_room_session_time():
    if request.method == "POST":
        session_id = request.form.get("session_id")
        new_time = request.form.get("new_time")
        update_session_time(session_id, new_time)
        flash("Session time updated successfully!", "success")
        return redirect(url_for("admin_view.manage_schedule"))
