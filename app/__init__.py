from flask import Flask
from app.config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up comfiguration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app.main import views
