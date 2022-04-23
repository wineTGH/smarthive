from flask import Flask

app = Flask(__name__)

from app import views

from api import error_handlers
from api import handlers