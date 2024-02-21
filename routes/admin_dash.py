from flask import render_template, Blueprint

admin_dash = Blueprint("admin_dash", __name__)


@admin_dash.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@admin_dash.route("/admin/billing", methods=["GET", "POST"])
def admin_billing():
    return render_template("admin_billing.html")
