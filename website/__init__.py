from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'config.py')
    app.config.from_pyfile(config_path)
    
    return app