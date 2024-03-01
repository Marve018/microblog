#!/usr/bin/python3
"""Flask application"""

from flask import Flask

app = Flask(__name__)

from app import routes
