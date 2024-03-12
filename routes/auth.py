from flask import render_template, request, redirect, url_for, session, Blueprint, flash
# import all the queries from the database.queries package that we need for the auth routes
from database.queries.member_queries import get_member_by_username, insert_new_member
# import the validate_password function from the util.helpers package
from util.helpers import validate_password

# creating a blueprint for the auth routes
auth = Blueprint("auth", __name__)


# creating a route for the login page
@auth.route("/login", methods=["GET", "POST"])
def login():
    # if the request method is POST
    if request.method == "POST":
        # get the user type, username, and password from the form
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        # get the user from the database by the username and user type
        user = get_member_by_username(user_type, username)

        # if the user exists and the password matches
        if user and user[2] == password: 
            # set the session variables and redirect to the dashboard
            session["username"] = username
            session["user_type"] = user_type
            session["member_id"] = user[0]
            # flash a success message
            flash(f"Logged in successfully!", "success")
            # redirect to the dashboard based on the user type
            if user_type == "Administrators":
                return redirect(url_for("admin_view.admin_dashboard"))
            elif user_type == "Members":
                return redirect(url_for("member_view.member_dashboard"))
            elif user_type == "Trainers":
                return redirect(url_for("trainer_view.trainer_dashboard"))
        # if the user does not exist or the password does not match
        flash("Invalid username or password.", "danger")
    # render the login page if the request method is GET
    return render_template("auth/login.html")


# creating a route for the register page
@auth.route("/register", methods=["GET", "POST"])
def register():
    # if the request method is POST
    if request.method == "POST":
        # get the user type, username, and password from the form
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        # get the user from the database by the username and user type
        user = get_member_by_username(user_type, username)
        # if the user exists, flash a warning message
        if user:
            flash(f"{user_type} {username} already exists.", "warning")
        # or if the password is invalid, flash a danger message
        elif not validate_password(password):
            flash("Password must be at least 6 characters long, and contain a number and an uppercase letter.", "danger")
    # if the user does not exist and the password is valid
        else:
            # insert the new member into the database 
            insert_new_member(user_type, username, password)
            # flash a success message and redirect to the register page
            flash(f"{user_type} {username} has been registered successfully", "success")
        return redirect(url_for("auth.login"))
    # if the request method is GET, render the register page
    return render_template("auth/register.html")


# creating a route for the logout page
@auth.route("/logout")
def logout():
    # clear the session and flash a message
    session.clear()
    flash("You have been logged out.", "info")
    # redirect to the login page
    return redirect(url_for("auth.login"))