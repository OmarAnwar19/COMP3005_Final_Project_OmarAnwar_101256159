from flask import render_template, Blueprint

admin_view = Blueprint("admin_view", __name__)


@admin_view.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/admin_dashboard.html")


@admin_view.route("/admin/billing", methods=["GET", "POST"])
def admin_billing():
    return render_template("admin/admin_billing.html")
