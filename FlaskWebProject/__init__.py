"""
The flask application package.
"""
import logging
from flask import Flask, session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask.logging import default_handler

app = Flask(__name__)
app.config.from_object(Config)
app.logger.removeHandler(default_handler)
app.logger.setLevel(logging.WARNING)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)
app.logger.warning('A new log has dawned!')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
