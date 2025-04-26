import flask

home = flask.Blueprint(
    name='home_app',
    import_name='home_app',
    template_folder='templates',
    static_folder='../static/home_app'
)