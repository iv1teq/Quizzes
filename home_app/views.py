import flask

def show_home_page():
    context = {'page': 'home', 'is_auth': True}
    return flask.render_template('home.html', **context)