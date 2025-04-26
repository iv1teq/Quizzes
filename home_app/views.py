import flask, flask_login

def show_home_page():
    if flask_login.current_user.is_authenticated:
        context = {'page': 'home', 'is_auth': flask_login.current_user.is_authenticated, 'name': flask_login.current_user.name}
    else:
        context = {'page': 'home', 'is_auth': flask_login.current_user.is_authenticated}
    return flask.render_template('home.html', **context)