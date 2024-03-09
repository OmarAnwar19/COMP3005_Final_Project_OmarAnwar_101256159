from flask import render_template, request, redirect, url_for, session, Blueprint, flash
from database.queries.member_queries import get_user_by_username, insert_user
from util.helpers import validate_password

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        user = get_user_by_username(user_type, username)

        if user and user[2] == password: 
            session["username"] = username
            session["user_type"] = user_type
            session["member_id"] = user[0]
            flash(f"Logged in successfully!", "success")
            if user_type == "Administrators":
                return redirect(url_for("admin_view.admin_dashboard"))
            elif user_type == "Members":
                return redirect(url_for("member_view.member_dashboard"))
            elif user_type == "Trainers":
                return redirect(url_for("trainer_view.trainer_dashboard"))
        flash("Invalid username or password.", "danger")
    return render_template("auth/login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        user = get_user_by_username(user_type, username)
        if user:
            flash(f"{user_type} {username} already exists.", "warning")
        elif not validate_password(password):
            flash("Password must be at least 6 characters long, and contain a number and an uppercase letter.", "danger")
        else:
            workouts_completed = 0
            sessions_booked = 0
            calories_burned = 0
            active_minutes = 0
            distance_covered = 0

            member_id = insert_user(user_type, username, password, workouts_completed, sessions_booked, calories_burned, active_minutes, distance_covered)
            flash(f"{user_type} {username} has been registered successfully", "success")
        return redirect(url_for("auth.register"))
    return render_template("auth/register.html")


@auth.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))