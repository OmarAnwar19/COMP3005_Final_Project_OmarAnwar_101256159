from flask import Flask, redirect, url_for, session
from database.db import setup_db
from database.keys import DB_KEY, SECRET

from routes.auth import auth
from routes.admin_view import admin_view
from routes.member_view import member_view
from routes.trainer_view import trainer_view

app = Flask(__name__)
app.secret_key = SECRET

with app.app_context():
    setup_db(app, DB_KEY)
    
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

app.register_blueprint(auth)
app.register_blueprint(admin_view)
app.register_blueprint(member_view)
app.register_blueprint(trainer_view)


# TODO: Add error handling for 404
# TODO: Add login / registration password checking
# TODO: Cleanup member dashboard and view
# TODO: Refactor and organize code

if __name__ == "__main__":
    app.run(debug=True)
