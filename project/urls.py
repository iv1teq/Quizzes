import home_app, history

from .settings import project

home_app.home.add_url_rule(rule= '/', view_func=home_app.show_home_page, methods = ['POST', 'GET'])

history.history.add_url_rule(rule= '/history',view_func=history.show_history_page, methods = ['POST', 'GET'])

project.register_blueprint(blueprint=home_app.home)

project.register_blueprint(blueprint=history.history)