from flask import render_template, Blueprint

trainer_dash = Blueprint("trainer_dash", __name__)

@trainer_dash.route("/trainer/dashboard")
def trainer_dashboard():
    return render_template("trainer_dashboard.html")


@trainer_dash.route("/trainer/schedule", methods=["GET", "POST"])
def trainer_schedule():
    return render_template("trainer_schedule.html")
