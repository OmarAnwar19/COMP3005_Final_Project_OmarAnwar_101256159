from flask import render_template, Blueprint, session, request, redirect, url_for, flash
from database.queries.admin_queries import *
from util.helpers import format_date, format_datetime

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
        print(new_date)
        update_equipment_maintenance_date(equipment_id, new_date)
        flash("Maintenance date updated.", "info")
        return redirect(url_for("admin_view.admin_dashboard"))