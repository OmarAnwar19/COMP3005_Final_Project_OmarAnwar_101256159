
from flask import render_template, request, redirect, url_for, session, Blueprint
from models import Member, Trainer, Admin
from database.db import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        if user_type == "member":
            user = Member.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session["username"] = username
                session["user_type"] = user_type
                return redirect(url_for("member_dashboard"))
        elif user_type == "trainer":
            user = Trainer.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session["username"] = username
                session["user_type"] = user_type
                return redirect(url_for("trainer_dashboard"))
        elif user_type == "admin":
            user = Admin.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session["username"] = username
                session["user_type"] = user_type
                return redirect(url_for("admin_dashboard"))
        return "Invalid username or password"
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_type = request.form.get("user_type")
        username = request.form.get("username")
        password = request.form.get("password")
        if user_type == "member":
            user = Member(username=username, password=password)
        elif user_type == "trainer":
            user = Trainer(username=username, password=password)
        elif user_type == "admin":
            user = Admin(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")