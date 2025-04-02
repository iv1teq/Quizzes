import flask

registration = flask.Blueprint(
    name='registration',
    import_name='registration',
    template_folder='registration/templates',
    static_folder='registation/static'
)