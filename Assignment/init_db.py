import sqlite3

connection = sqlite3.connect('zfschool1.db')


with open('schema/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# create a cursor object that is required to process rows in a database
# the cursor object is necessary to read through the database

# Use the cursors execute method to run SQL statements
cur.execute('INSERT INTO student (fname, lname, email, password, DOB, gender, house, tutor_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            ('Oska', 'Fenwick', 'oskafenwick@stpauls.qld.edu.au', 'mniof2008', '1976-06-05', 'Male', 'Gladius', 'G04')
            )
connection.commit()
cur.execute('INSERT INTO tutors (fname, lname, email, password, DOB, gender, house, tutor_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            ('Mel', 'Johnson', 'meljohnson@stpauls.qld.edu.au', 'michealjordan', '1984-03-23', 'Female', 'Gladius', 'G01')
            )
connection.commit()

# TUTOR GROUPS EACH HOUSE AND NUMBER

cur.execute('INSERT INTO tutor_groups (id, room, teacher, house, points) VALUES (?, ?, ?, ?, ?)',
            ('G01','R1', 'Mel Johnson', 'Gladius', 0)
            )
connection.commit()

def inserttgroup(tutor_details):
    con=sqlite3.connect('zfschool1.db')
    c=con.cursor()
    sql_execute_string='INSERT INTO tutor_groups (id, house, points) VALUES (?, ?, ?)'
    c.execute(sql_execute_string,tutor_details)
    con.commit()


G02=(
    'G02',
    'Gladius',
    0
)
G03=(
    'G03',
    'Gladius',
    0
)
G04=(
    'G04',
    'Gladius',
    0
)
G05=(
    'G05',
    'Gladius',
    0
)
G06=(
    'G06',
    'Gladius',
    0
)
G07=(
    'G07',
    'Gladius',
    0
)
G08=(
    'G08',
    'Gladius',
    0
)
G09=(
    'G09',
    'Gladius',
    0
)
M01=(
    'M01',
    'Mitre',
    0
)
M02=(
    'M02',
    'Mitre',
    0
)
M03=(
    'M03',
    'Mitre',
    0
)
M04=(
    'M04',
    'Mitre',
    0
)
M05=(
    'M05',
    'Mitre',
    0
)
M06=(
    'M06',
    'Mitre',
    0
)
M07=(
    'M07',
    'Mitre',
    0
)
M08=(
    'M08',
    'Mitre',
    0
)
M09=(
    'M09',
    'Mitre',
    0
)
S01=(
    'S01',
    'Scudo',
    0
)
S02=(
    'S02',
    'Scudo',
    0
)
S03=(
    'S03',
    'Scudo',
    0
)
S04=(
    'S04',
    'Scudo',
    0
)
S05=(
    'S05',
    'Scudo',
    0
)
S06=(
    'S06',
    'Scudo',
    0
)
S07=(
    'S07',
    'Scudo',
    0
)
S08=(
    'S08',
    'Scudo',
    0
)
S09=(
    'S09',
    'Scudo',
    0
)
T01=(
    'T01',
    'Taja',
    0
)
T02=(
    'T02',
    'Taja',
    0
)
T03=(
    'T03',
    'Taja',
    0
)
T04=(
    'T04',
    'Taja',
    0
)
T05=(
    'T05',
    'Taja',
    0
)
T06=(
    'T06',
    'Taja',
    0
)
T07=(
    'T07',
    'Taja',
    0
)
T08=(
    'T08',
    'Taja',
    0
)
T09=(
    'T09',
    'Taja',
    0
)
B01=(
    'B01',
    'Boek',
    0
)
B02=(
    'B02',
    'Boek',
    0
)
B03=(
    'B03',
    'Boek',
    0
)
B04=(
    'B04',
    'Boek',
    0
)
B05=(
    'B05',
    'Boek',
    0
)
B06=(
    'B06',
    'Boek',
    0
)
B07=(
    'B07',
    'Boek',
    0
)
B08=(
    'B08',
    'Boek',
    0
)
B09=(
    'B09',
    'Boek',
    0
)
# Gladius Tutor Groups
inserttgroup(G02)
inserttgroup(G03)
inserttgroup(G04)
inserttgroup(G05)
inserttgroup(G06)
inserttgroup(G07)
inserttgroup(G08)
inserttgroup(G09)

# Mitre Tutor Groups
inserttgroup(M01)
inserttgroup(M02)
inserttgroup(M03)
inserttgroup(M04)
inserttgroup(M05)
inserttgroup(M06)
inserttgroup(M07)
inserttgroup(M08)
inserttgroup(M09)

# Scudo Tutor Groups
inserttgroup(S01)
inserttgroup(S02)
inserttgroup(S03)
inserttgroup(S04)
inserttgroup(S05)
inserttgroup(S06)
inserttgroup(S07)
inserttgroup(S08)
inserttgroup(S09)

# Taja Tutor Groups
inserttgroup(T01)
inserttgroup(T02)
inserttgroup(T03)
inserttgroup(T04)
inserttgroup(T05)
inserttgroup(T06)
inserttgroup(T07)
inserttgroup(T08)
inserttgroup(T09)

# Boek Tutor Groups
inserttgroup(B01)
inserttgroup(B02)
inserttgroup(B03)
inserttgroup(B04)
inserttgroup(B05)
inserttgroup(B06)
inserttgroup(B07)
inserttgroup(B08)
inserttgroup(B09)

cur.execute('INSERT INTO houses (name, house_leader, points) VALUES (?, ?, ?)',
            ('Gladius', 'Neil White', 0)
            )
connection.commit()
cur.execute('INSERT INTO houses (name, house_leader, points) VALUES (?, ?, ?)',
            ('Mitre', 'David Fenwick', 0)
            )
connection.commit()
cur.execute('INSERT INTO houses (name, house_leader, points) VALUES (?, ?, ?)',
            ('Taja', 'Des Hylton', 0)
            )
connection.commit()
cur.execute('INSERT INTO houses (name, house_leader, points) VALUES (?, ?, ?)',
            ('Scudo', 'Sophie Hughes', 0)
            )
connection.commit()
cur.execute('INSERT INTO houses (name, house_leader, points) VALUES (?, ?, ?)',
            ('Boek', 'Lisa Bolger', 0)
            )
connection.commit()
cur.execute('INSERT INTO activities (name, description, points) VALUES (?, ?, ?)',
            ('Koala Corridor', 'Planting trees for Koala passage', 10)
            )
connection.commit()
cur.execute('INSERT INTO attendance (name, act_date, act_time) VALUES (?, ?, ?)',
            ('Koala Corridor', '2022-09-16', '12:00')
            )
# Commit changes to the database and close the database
connection.commit()
cur.execute('INSERT INTO participants (student, act_id) VALUES (?, ?)',
            ('oskafenwick@stpauls.qld.edu.au', '1')
            )
connection.commit()


connection.close()
