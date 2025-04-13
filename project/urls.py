import home_app

from .settings import project

home_app.home.add_url_rule(rule= '/', view_func=home_app.show_home_page, methods = ['POST', 'GET'])

project.register_blueprint(blueprint=home_app.home)