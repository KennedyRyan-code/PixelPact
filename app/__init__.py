#!/usr/bin/python3
"""initialize the models package"""

from flask import Flask

app = Flask(__name__)

from app.web_flask import routes
