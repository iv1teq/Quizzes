from flask_login import login_required, current_user, logout_user
from flask import redirect, url_for
import flask

@login_required
def show_profile_page():
    context = {
        'page': 'profile',
        'name': current_user.name,
        'email': current_user.email,
    }
    return flask.render_template("profile.html", **context)

@login_required
def logout():
    logout_user()  
    return redirect(url_for('home_app.show_home_page'))  

