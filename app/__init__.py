from flask import Flask
from flask-bootstrap import Bootstrap
from config import config_options

# Initialize bootstrap
bootstrap = Bootstrap()


def create_app(config_name):
    """Function to create the application instance - Application Factory"""
    
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing boostrap
    bootstrap.init_app(app)

    return app
