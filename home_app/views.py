import flask

def show_home_page():
    return flask.render_template('home.html')