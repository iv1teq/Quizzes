import flask,os


DIR=os.path.abspath(os.path.dirname(__file__))

join = flask.Blueprint(
    name= "join",
    import_name = "join",
    template_folder='templates',
    static_folder=os.path.join(DIR, "static"),
    static_url_path="/join"
)