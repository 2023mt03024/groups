# reference: https://www.digitalocean.com/community/tutorials/
#            how-to-make-a-web-application-using-flask-in-python-3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_group(group_id):
    conn = get_db_connection()
    group = conn.execute('SELECT * FROM groups WHERE id = ?',
                        (group_id,)).fetchone()
    conn.close()
    if group is None:
        abort(404)
    return group

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    groups = conn.execute('SELECT * FROM groups').fetchall()
    conn.close()
    return render_template('index.html', groups=groups)

@app.route('/about')
def about():
      return render_template('about.html')

@app.route('/<int:group_id>')
def group(group_id):
    group = get_group(group_id)
    return render_template('group.html', group=group)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        member1 = request.form['member1']
        member2 = request.form['member2']
        member3 = request.form['member3']
        member4 = request.form['member4']
        member5 = request.form['member5']

        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO groups (name, member1, member2, member3, member4, member5) VALUES (?, ?, ?, ?, ?, ?)',
                         (name, member1, member2, member3, member4, member5))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    group = get_group(id)

    if request.method == 'POST':
        name = request.form['name']
        member1 = request.form['member1']
        member2 = request.form['member2']
        member3 = request.form['member3']
        member4 = request.form['member4']
        member5 = request.form['member5']

        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE groups SET name = ?, member1 = ?, member2 = ?, member3 = ?, member4 = ?, member5 = ?'
                         ' WHERE id = ?',
                         (name, member1, member2, member3, member4, member5, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', group=group)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    group = get_group(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM groups WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(group['name']))
    return redirect(url_for('index'))
