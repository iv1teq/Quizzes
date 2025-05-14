
import flask
from flask_login import  current_user

def render_join():
    context = {'page': 'home',
               'is_auth': current_user.is_authenticated,
               'name': current_user.name}
    return flask.render_template(template_name_or_list='join.html', **context)