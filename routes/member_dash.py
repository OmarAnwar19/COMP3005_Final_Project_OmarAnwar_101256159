from flask import render_template, Blueprint

member_dash = Blueprint("member_dash", __name__)

@member_dash.route("/member/dashboard")
def member_dashboard():
    return render_template("member_dashboard.html")


@member_dash.route("/member/profile", methods=["GET", "POST"])
def member_profile():
    return render_template("member_profile.html")