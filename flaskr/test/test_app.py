"""App test file.
"""

from . import FlaskrTestCase


class TestApp(FlaskrTestCase):
    def test_home(self):
        res = self.app.get('/test')
        data = res.data.decode()
        self.assertEqual(data, 'Hello World')

    def test_login(self):
        res = self.app.get('/login')
        self.assertEqual(res.status_code, 200)

    def test_random(self):
        res = self.app.get('/random')
        self.assertEqual(res.status_code, 404)

    def test_empty_db(self):
        rv = self.app.get('/')
        self.assertTrue(b'No entries here so far' in rv.data)

    def test_auth(self):
        # Make sure login/logout streams are working properly
        rv = self.login(self.config['USERNAME'], self.config['PASSWORD'])
        self.assertTrue(b'You were logged in!' in rv.data)
        rv = self.logout()
        self.assertTrue(b'You were logged out!' in rv.data)
        rv = self.login('bad', self.config['PASSWORD'])
        self.assertTrue(b'Invalid username.' in rv.data)
        rv = self.login(self.config['USERNAME'], 'bad')
        self.assertTrue(b'Invalid password.' in rv.data)

    def test_messages(self):
        # Make sure that posts work correctly
        self.login(self.config['USERNAME'], self.config['PASSWORD'])
        res = self.app.post('/add', data=dict(title='Hi',
                                              text='HTML here!'),
                            follow_redirects=True)

        self.assertTrue(b'No entries here so far' not in res.data)
        self.assertTrue(b'Hi' in res.data)
        self.assertTrue(b'HTML here!' in res.data)
