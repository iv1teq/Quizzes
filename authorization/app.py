import flask 
authorization = flask.Blueprint(
    name = "authorization",
    import_name = "authorization",
    template_folder = "templates",
    static_folder = "../static/science_and_entertainment_quiz",
                                )