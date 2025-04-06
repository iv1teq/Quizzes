import flask

def render_new_quiz():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App.html', **context)