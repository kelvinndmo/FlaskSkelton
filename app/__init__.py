from flask import Flask
from config import config_options

# create an application factory
def create_app(config_name):
    """
    creates an instances of the application 
    and passes the config name, i.e development
    or production, the will then pick the environments
    from the configuration classes in config
    """

    app = Flask(__name__)



    # set the configurations
    app.config.from_object(config_options[config_name])

    #register your blueprints here
    from main import main
    app.register_blueprint(main)


    return app