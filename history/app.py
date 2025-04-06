import flask

history = flask.Blueprint(
    name= "history" ,
    import_name = "history",
    template_folder= "templates",
    static_folder= "../static/"
)