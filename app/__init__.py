from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

from app import views

from app.api import error_handlers
from app.api import hive_handlers