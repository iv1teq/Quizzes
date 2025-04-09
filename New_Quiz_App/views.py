import flask

def render_new_quiz():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App.html', **context)

def render_new_quiz_2():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_App_2.html', **context)

def render_new_quiz_settigs():
    context = {'page': 'home'}
    return flask.render_template('New_Quiz_Settings.html', **context)