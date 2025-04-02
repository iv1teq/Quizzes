import flask

New_Quiz = flask.Blueprint(
  name = "New_Quiz",
  import_name = "New_Quiz_App",
  template_folder = "templates",
  static_folder = "static",
)