import argparse
from flask import Flask, redirect, url_for, session, render_template, request, abort
from database.keys import SECRET

# importing blueprints for all the different routes
from routes.auth import auth
from routes.admin_view import admin_view
from routes.member_view import member_view
from routes.trainer_view import trainer_view

app = Flask(__name__)
app.secret_key = SECRET


# this function restricts access to certain routes based on the user's role
@app.before_request
def restrict_access_based_on_role():
    user_type = session.get("user_type")
    # if the user's role is not the same as the route's role, then they are not allowed to access the route
    if ((user_type == "Members" and (request.path.startswith("/admin") or request.path.startswith("/trainer")))
        or (user_type == "Trainers" and (request.path.startswith("/admin") or request.path.startswith("/member")))
        or (user_type == "Administrators" and (request.path.startswith("/member") or request.path.startswith("/trainer")))):
        abort(403) # this will return a 403 error page
        

# this function redirects the user to their dashboard based on their role
@app.route("/") 
def index(): 
    # if the user is not logged in, they are redirected to the login page
    if "username" not in session: 
        return redirect(url_for("auth.login")) 
    else: 
        # if the user is logged in, they are redirected to their dashboard based on their role
        user_type = session.get("user_type") 
        if user_type == "Members": 
            return redirect(url_for("member_view.member_dashboard")) 
        elif user_type == "Trainers": 
            return redirect(url_for("trainer_view.trainer_dashboard")) 
        elif user_type == "Administrators": 
            return redirect(url_for("admin_view.admin_dashboard"))


# these functions handle different error pages
@app.errorhandler(403)
def unauthorized_access(e):
    # if the user tries to access a route that they are not allowed to, they will be redirected to a 403 error page
    return render_template("403.html"), 403

@app.errorhandler(404)
def page_not_found(e):
    # if the user tries to access a route that does not exist, they will be redirected to a 404 error page
    return render_template("404.html"), 404


# registering the blueprints for all the different routes
app.register_blueprint(auth)
app.register_blueprint(admin_view)
app.register_blueprint(member_view)
app.register_blueprint(trainer_view)


if __name__ == "__main__":
    # adding a command line argument to run the app in debug mode
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Run in debug mode.")
    args = parser.parse_args()
    # the app runs in debug mode if the --debug argument is passed
    app.run(debug=args.debug)