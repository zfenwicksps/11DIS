import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('blogposts.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    houses = conn.execute('SELECT * FROM houses').fetchall()
    conn.close()
    return render_template('index.html', houses=houses)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fname = request.form['title']
        lname = request.form['content']

        if not fname:
            flash('First Name is required!')
        elif not lname:
            flash('Last Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO student (title, content) VALUES (?, ?)',
                         (fname, lname))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

#if __name__ == '__main__':
    # run app in debug mode on port 5000
    #app.run(debug=True, port=5000)
