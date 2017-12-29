"""App test file.
"""

import unittest

from flaskr.flaskr import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        res = self.app.get('/test')
        data = res.data.decode()
        self.assertEqual(data, 'Hello World')
