import argparse
from flask import Flask, redirect, url_for, session, render_template
from database.keys import SECRET

from routes.auth import auth
from routes.admin_view import admin_view
from routes.member_view import member_view
from routes.trainer_view import trainer_view

app = Flask(__name__)
app.secret_key = SECRET
    
@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("auth.login"))
    else:
        user_type = session.get("user_type")
        if user_type == "Members":
            return redirect(url_for("member_view.member_dashboard"))
        elif user_type == "Trainers":
            return redirect(url_for("trainer_view.trainer_dashboard"))
        elif user_type == "Administrators":
            return redirect(url_for("admin_view.admin_dashboard"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

app.register_blueprint(auth)
app.register_blueprint(admin_view)
app.register_blueprint(member_view)
app.register_blueprint(trainer_view)


# TODO: Password validation on update profile
# TODO: Complete trainer dashboard and view
# TODO: Complete admin dashboard and view
# TODO: Refactor and organize code

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Run in debug mode.")
    args = parser.parse_args()
    app.run(debug=args.debug)