"""This module is called by Google App Engine

It looks for "app" in the "main.py" class to run flask with gunicorn"""
import logging
from flask import Flask
from pandas import DataFrame
from flask.logging import create_logger
from webapp.database import  test_gets

gets = test_gets
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
log = create_logger(app)
log.info('------ DEBUG LOGGING STARTS HERE -------')

from webapp.routes import route