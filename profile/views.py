from flask_login import login_required, current_user
import flask

@login_required
def show_profile_page():
    context = {
        'page': 'profile',
        'name': current_user.name,
        'email': current_user.email  
    }
    return flask.render_template("profile.html", **context)

   



