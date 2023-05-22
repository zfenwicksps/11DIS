import sqlite3

# create a connection to the database
connection = sqlite3.connect('blogposts.db')


# read in the schema file
with open('schemas/schema.sql') as f:
    connection.executescript(f.read())

# create a cursor object that is required to process rows in a database
# the cursor object is necessary to read through the database
cur = connection.cursor()

# Use the cursors execute method to run SQL statements
cur.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            ('First Post', 'Content for the first post')
            )

cur.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            ('Second Post', 'Content for the second post'))

# Commit changes to teh database and close the database
connection.commit()
connection.close()
