"""Main run file.
"""

from flaskr import app

app.run(debug=app.config['DEBUG'],
        host='0.0.0.0',
        port=app.config['PORT'])
