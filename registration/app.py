import flask

registration = flask.Blueprint(
    name='registration',
    import_name='registration',
    template_folder='templates',
    static_folder='../static/registation'
)