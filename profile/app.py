import flask,os


DIR  =os.path.abspath(os.path.dirname(__file__))
profille = flask.Blueprint(
    name= "profile" ,
    import_name = "profile",
    template_folder='templates',
    static_folder=os.path.join(DIR,"static"),
    static_url_path="/profile"
)

