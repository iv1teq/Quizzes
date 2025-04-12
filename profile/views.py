import flask

def show_profile_page():
    context = {'page': 'home'}
    return flask.render_template(template_name_or_list="profile.html", **context )
   