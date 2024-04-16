#app/__init__.py
from flask import Flask
from .views import main_blueprint

def create_app():
  app = Flask(__name__)
