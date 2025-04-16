import flask 
def show_authorization():
    context={'page': 'authorization'}
    return flask.render_template("authorization.html", **context)