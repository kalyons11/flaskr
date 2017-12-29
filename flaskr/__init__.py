"""Main app file.
"""

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# Create app instance
app = Flask(__name__)

# Load config
app.config.from_object('config')


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


# Simple route
@app.route('/test')
def test_page():
    return 'Hello World'
