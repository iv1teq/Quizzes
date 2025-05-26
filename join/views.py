
import flask


def render_join():
    context = {'page': 'home'}
    return flask.render_template(template_name_or_list='join.html', **context)