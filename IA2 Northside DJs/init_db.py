import sqlite3
connection = sqlite3.connect('northsidedj.db')

with open('schema/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# create a cursor object that is required to process rows in a database
# the cursor object is necessary to read through the database

# Use the cursors execute method to run SQL statements

cur.execute('INSERT INTO users (fname, lname, email, password, DJ, DJ_type) VALUES (?, ?, ?, ?, ?, ?)',
            ('Anthony', 'Jones', 'anthonyjones@gmail.com', 'ajthedj', True, 'party')
            )
connection.commit()
cur.execute('INSERT INTO users (fname, lname, email, password, DJ, DJ_type) VALUES (?, ?, ?, ?, ?, ?)',
            ('Devin', 'Dangerfield', 'devindangerfield@gmail.com', 'djdangerfield', True, 'rave')
            )
connection.commit()
cur.execute('INSERT INTO users (fname, lname, email, password, DJ, DJ_type) VALUES (?, ?, ?, ?, ?, ?)',
            ('Betty', 'Becks', 'bettybecks@gmail.com', 'djbecks', True, 'wedding')
            )
connection.commit()
cur.execute('INSERT INTO users (fname, lname, email, password, DJ, DJ_type) VALUES (?, ?, ?, ?, ?, ?)',
            ('Sarah', 'Star', 'sarahstar@gmail.com', 'djstar', True, 'club')
            )
connection.commit()
cur.execute('INSERT INTO users (fname, lname, email, password, DJ, DJ_type) VALUES (?, ?, ?, ?, ?, ?)',
            ('Jeffrey', 'Jazei', 'jeffreyjazei@gmail.com', 'djjazei', True, 'formal')
            )
connection.commit()
connection.close()
