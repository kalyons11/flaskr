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


def init_db():
    """Sets up db for us.
    """
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


def connect_db():
    """Connects to the specific database.
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request.
    """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# Simple route
@app.route('/test')
def test_page():
    return 'Hello World'


# Entries route
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


# Addd new entry
@app.route('/add', methods=['POST'])
def add_entry():
    # Validate login
    if not session.get('logged_in'):
        abort(404)

    # Make query
    db = get_db()
    db.execute('INSERT INTO entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()

    # Alert user
    flash('New entry posted!')
    return redirect(url_for('show_entries'))


# Handle login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Set err var for later
    err = None

    # Handle post case
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            err = 'Invalid username.'
        elif request.form['password'] != app.config['PASSWORD']:
            err = 'Invalid password.'
        else:
            session['logged_in'] = True
            flash('You were logged in!')
            return redirect(url_for('show_entries'))

    return render_template('login.html', error=err)


# Handle logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out!')
    return redirect(url_for('show_entries'))
