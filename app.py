from flask import Flask, redirect, url_for, session
from database.db import setup_db
from database.keys import DB_KEY

from routes.auth import auth
from routes.admin_dash import admin_dash
from routes.member_dash import member_dash
from routes.trainer_dash import trainer_dash

app = Flask(__name__)

with app.app_context():
    setup_db(app, DB_KEY)
    
@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("auth.login"))
    else:
        user_type = session.get("user_type")
        if user_type == "member":
            return redirect(url_for("member_dashboard"))
        elif user_type == "trainer":
            return redirect(url_for("trainer_dashboard"))
        elif user_type == "admin":
            return redirect(url_for("admin_dashboard"))


app.register_blueprint(auth)
app.register_blueprint(admin_dash)
app.register_blueprint(member_dash)
app.register_blueprint(trainer_dash)


if __name__ == "__main__":
    app.run(debug=True)
