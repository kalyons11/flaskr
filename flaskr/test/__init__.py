"""Main test file.
"""

import os
import tempfile
import unittest

import flaskr
import nose


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        self.config = flaskr.app.config
        with flaskr.app.app_context():
            flaskr.flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def login(self, username, password):
        """Quick method to handle login.
        """
        return self.app.post('/login',
                             data=dict(username=username,
                                       password=password),
                             follow_redirects=True)

    def logout(self):
        """Quick method to handle logout.
        """
        return self.app.get('/logout', follow_redirects=True)
