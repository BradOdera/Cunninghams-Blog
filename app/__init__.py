from flask import Flask
from app.config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
# Setting up comfiguration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


def create_app(config_name):
    app = Flask(__name__)
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

from app.main import views