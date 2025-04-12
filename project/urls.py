import home_app
from profile.app import profille
from profile.views import show_profile_page
from .settings import project


home_app.home.add_url_rule(rule= '/', view_func=home_app.show_home_page, methods = ['POST', 'GET'])


project.register_blueprint(blueprint=home_app.home)


profille.add_url_rule(rule= '/profile', view_func=show_profile_page, methods = ['POST', 'GET'])

project.register_blueprint(blueprint=profille)