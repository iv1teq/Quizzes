import flask

profile = flask.Blueprint(
    name= "profile" ,
    import_name = "profile",
    template_folder= "profile/templates",
    static_folder= "profile/static"
)