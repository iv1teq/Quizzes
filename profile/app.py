import flask

profille = flask.Blueprint(
    name= "profile" ,
    import_name = "profile",
    template_folder='templates',
    static_folder='../static/profile'
)