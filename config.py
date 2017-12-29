"""Main app config file.
"""

import os

DATABASE = os.getenv('DATABASE')
SECRET_KEY = os.getenv('SECRET_KEY')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
DEBUG = bool(os.getenv('DEBUG'))
PORT = int(os.getenv('PORT'))
