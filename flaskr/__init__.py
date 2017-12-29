"""Main app file.
"""

from flask import Flask

app = Flask(__name__)


# Simple route
@app.route('/test')
def test_page():
    return 'Hello World'
