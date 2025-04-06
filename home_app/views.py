import flask

def show_home_page():
    context = {'page': 'home'}
    return flask.render_template('home.html', **context)