from flask import render_template, Blueprint

trainer_view = Blueprint("trainer_view", __name__)

@trainer_view.route("/trainer/dashboard")
def trainer_dashboard():
    return render_template("trainer/trainer_dashboard.html")


@trainer_view.route("/trainer/schedule", methods=["GET", "POST"])
def trainer_schedule():
    return render_template("trainer/trainer_schedule.html")
