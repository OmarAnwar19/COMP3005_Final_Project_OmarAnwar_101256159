from flask import render_template, request, redirect, url_for, session, Blueprint, flash
from database.raw_queries import get_user_by_username, insert_user

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
            if user_type == "Administrators":
                return redirect(url_for("admin_dash.admin_dashboard"))
            elif user_type == "Members":
                return redirect(url_for("member_dash.member_dashboard"))
            elif user_type == "Trainers":
                return redirect(url_for("trainer_dash.trainer_dashboard"))
        flash("Error. Invalid username or password.")
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        user = get_user_by_username(user_type, username)
        if user:
            flash(f"{user_type} {username} already exists.")
        else:
            insert_user(user_type, username, password)
            flash(f"{user_type} {username} has been registered successfully")
        return redirect(url_for("auth.login"))
    return render_template("register.html")