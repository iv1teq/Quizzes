import home_app, history

from .settings import project

home_app.home.add_url_rule(rule= '/', view_func=home_app.show_home_page, methods = ['POST', 'GET'])

history.history.add_url_rule(rule='/history', view_func=history.show_history_page)
history.history.add_url_rule(rule='/qsr', view_func=history.show_qsr_page)
history.history.add_url_rule(rule='/qtr', view_func=history.show_qtr_page)


project.register_blueprint(blueprint=home_app.home)
project.register_blueprint(blueprint=history.history)