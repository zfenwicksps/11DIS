import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = 'mysupersecretkey'


### use models to create functions for inserting, deleting, retrieval and connection and call upon it in app.py

########
# Connecting to the database
# This is one of the ways I used to connect to the database and get or post information
def get_db_connection():
    conn = sqlite3.connect('zfschool1.db')
    conn.row_factory = sqlite3.Row  # Way of returning sql data
    return conn


@app.route("/")
@app.route("/index")
def index():
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM student').fetchall()
    # .fetchone returns first row in table
    # .fetchall returns all rows in table
    conn.close()
    return render_template('index.html', student=student)


@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('role', None)
    session.pop('house', None)
    return redirect(url_for('index'))


@app.route("/points")
def points():
    conn = get_db_connection()
    houses = conn.execute('SELECT * FROM houses').fetchall()
    conn.close()


    con = sqlite3.connect('zfschool1.db')
    c = con.cursor()
    # The code below is getting the points from each tutor group and adding them together to then display the total
    # house points. This is done for each house
    gTotal = c.execute("SELECT points FROM tutor_groups WHERE house = 'Gladius'").fetchall()
    gList = []
    #print(gTotal)
    for g in gTotal:
        g = str(g).strip('(,)')
        g = int(g)
        gList.append(g)
    gladius = str(sum(gList))

    mTotal = c.execute("SELECT points FROM tutor_groups WHERE house = 'Mitre'").fetchall()
    mList = []
    for m in mTotal:
        m = str(m).strip('(,)')
        m = int(m)
        mList.append(m)
    mitre = str(sum(mList))

    tTotal = c.execute("SELECT points FROM tutor_groups WHERE house = 'Taja'").fetchall()
    tList = []
    for t in tTotal:
        t = str(t).strip('(,)')
        t = int(t)
        tList.append(t)
    taja = str(sum(tList))

    sTotal = c.execute("SELECT points FROM tutor_groups WHERE house = 'Scudo'").fetchall()
    sList = []
    for s in sTotal:
        s = str(s).strip('(,)')
        s = int(s)
        sList.append(s)
    scudo = str(sum(sList))

    bTotal = c.execute("SELECT points FROM tutor_groups WHERE house = 'Boek'").fetchall()
    bList = []
    for b in bTotal:
        b = str(b).strip('(,)')
        b = int(b)
        bList.append(b)
    boek = str(sum(bList))

    # Updating the houses points
    c.execute("UPDATE houses SET points = '"+gladius+"' WHERE name = 'Gladius'")
    c.execute("UPDATE houses SET points = '"+mitre+"' WHERE name = 'Mitre'")
    c.execute("UPDATE houses SET points = '"+taja+"' WHERE name = 'Taja'")
    c.execute("UPDATE houses SET points = '"+scudo+"' WHERE name = 'Scudo'")
    c.execute("UPDATE houses SET points = '"+boek+"' WHERE name = 'Boek'")




    con.commit()
    con.close()


    if session.get('username'):
#        print(session['house'])
        house = ''.join(session['house'][0])
#        print(house)
#        print(type(house))
        if house == 'Gladius':
            conn = get_db_connection()

            points = conn.execute('SELECT id, points FROM tutor_groups WHERE house = "Gladius"').fetchall()
            #print(points)
            ### ERROR
            #house = 'Gladius'
            #points = c.execute("""SELECT id, points FROM tutor_groups WHERE house = VALUES (?)""", (house))

            #points = c.execute(query, (house)).fetchall()
            #print(points)
            #print(type(points))
            conn.close()

        elif house == 'Mitre':
            conn = get_db_connection()
            points = conn.execute('SELECT id, points FROM tutor_groups WHERE house = "Mitre"').fetchall()
            conn.close()

        elif house == 'Taja':
            conn = get_db_connection()
            points = conn.execute('SELECT id, points FROM tutor_groups WHERE house = "Taja"').fetchall()
            conn.close()

        elif house == 'Scudo':
            conn = get_db_connection()
            points = conn.execute('SELECT id, points FROM tutor_groups WHERE house = Scudo').fetchall()
            conn.close()

        else:
            conn = get_db_connection()
            points = conn.execute('SELECT id, points FROM tutor_groups WHERE house = Boek').fetchall()
            conn.close()

    else:
        points = 'No Data'


    print(houses)
    return render_template('points.html', houses=houses, points=points)


def tutor_pts(house):
    con = sqlite3.connect('zfschool1.db')
    c = con.cursor()
    points = c.execute('SELECT id, points FROM tutor_groups WHERE house = "' + house + '"').fetchall()
    print(points)
    con.close()
    return points


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    elif request.method == "GET":
        return render_template("register.html")
    else:
        number = request.form['tutor_id']
        house = request.form['house']
        if house == 'Gladius':
            tutor_id = f'G{number}'
        elif house == 'Mitre':
            tutor_id = f'M{number}'
        elif house == 'Taja':
            tutor_id = f'T{number}'
        elif house == 'Scudo':
            tutor_id = f'S{number}'
        else:
            tutor_id = f'B{number}'

        user_details = (
            request.form['fname'],
            request.form['lname'],
            request.form['email'],
            request.form['password'],
            request.form['DOB'],
            request.form['gender'],
            request.form['house'],
            tutor_id

        )
        house_details = (
            request.form['fname'],
            request.form['lname'],
            request.form['email'],
            request.form['password'],
            request.form['DOB'],
            request.form['gender'],
            request.form['house']

        )
        if request.form['role'] == "student":
            insertstudent(user_details)
        elif request.form['role'] == "tutor":
            inserttutor(user_details)
        else:
            inserthouse(house_details)
        # flash('You are successfully registered!', "success")
        return render_template("registersuccess.html")


def insertstudent(user_details):
    con = sqlite3.connect('zfschool1.db')
    c = con.cursor()
    sql_execute_string = 'INSERT INTO student (fname, lname, email, password, DOB, gender, house, tutor_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    c.execute(sql_execute_string, user_details)
    con.commit()
    con.close()


def inserttutor(user_details):
    con = sqlite3.connect('zfschool1.db')
    c = con.cursor()
    sql_execute_string = 'INSERT INTO tutors (fname, lname, email, password, DOB, gender, house, tutor_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    c.execute(sql_execute_string, user_details)
    con.commit()
    con.close()


def inserthouse(house_details):
    con = sqlite3.connect('zfschool1.db')
    c = con.cursor()
    sql_execute_string = 'INSERT INTO tutors (fname, lname, email, password, DOB, gender, house) VALUES (?, ?, ?, ?, ?, ?, ?)'
    c.execute(sql_execute_string, house_details)
    con.commit()
    con.close()


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    elif request.method == 'POST':
        con = sqlite3.connect('zfschool1.db')
        c = con.cursor()

        email = request.form['email']
        password = request.form['password']
        role = request.form['role'].lower()
        print(role)
        if request.form['role'].lower() == 'house':
            role = 'tutors'

        results = c.execute(
            'SELECT email, password FROM "' + role + '" where email= "' + email + '" AND password= "' + password + '" ').fetchall()


        #results = stuff.fetchall()

        if len(results) == 0:
            return render_template("unsuccessful.html")
        # Incorrect username or password
        else:

            session['username'] = email


            session['house'] = c.execute('SELECT house FROM "' + role + '" WHERE email= "' + email + '"').fetchall()
            if request.form['role'].lower() == 'house':
                role = 'houseleader'
            session['role'] = role
            return render_template("loginsuccess.html")

    #    c.execute('SELECT fname, password FROM "'+role+'" where fname= "'+fname+'" AND password= "'+password+'" ')

    #    id = c.execute('SELECT id FROM "'+role+'" WHERE ')

    return render_template("login.html")


@app.route("/activities", methods=['GET', 'POST'])
@app.route("/activitiesAttend", methods=['GET', 'POST'])
def activities():
    con = get_db_connection()
    query = con.execute('SELECT * FROM activities').fetchall()
    attendance = con.execute('SELECT id, name, act_date AS date, act_time as time FROM attendance').fetchall()
    con.close()
    if request.method == 'POST':
        if session['role'] == 'student':
            con = sqlite3.connect('zfschool1.db')
            c = con.cursor()

            date_time = request.form['date'].split()
            user_details = c.execute('SELECT * FROM "'+session['role']+'" WHERE email = "'+session['username']+'"').fetchall()
            #print(user_details)
            #print(type(user_details))
            #print(len(user_details))
            #print(user_details[0])
            for user in user_details:
                tutor = user[9]
            #for user in user_details:
            #    print(type(user))
            #print(date_time)
            #print(date_time[0])
            #print(session['house'])
            attend = 1
            i = c.execute('SELECT id FROM attendance '
                             'WHERE act_date = "'+date_time[1]+'" AND act_time = "'+date_time[0]+'"').fetchall()
            id = str(i).strip('[(,)]')
            results = c.execute('SELECT student, act_id FROM participants').fetchall()
            for res in results:
                if res[0] == session['username'] and res[1] == id:
                    attend = None
                    break

            if attend != None:
                n = c.execute('SELECT name FROM attendance '
                                 'WHERE act_date = "'+date_time[1]+'" AND act_time = "'+date_time[0]+'"').fetchall()
                name = str(n).strip("[(,'')]")
                #print(name)
                z = c.execute('SELECT points FROM activities WHERE name = "'+name+'"').fetchall()
                zp = str(z).strip("[(,)]")
                fpts = int(zp)
                print(fpts)
                #print(i)
                #print(type(i))
                #print(i[0])
                #print(type(i[0]))
                #for d in i:
                #    print(d)
                #    print(type(d))
                #print(id)
                #print(session['id'])
                #print(id)
                #print(type(id))
                print(session['username'])
                p = c.execute('SELECT points FROM tutor_groups WHERE id = "'+tutor+'"').fetchall()
                point = str(p).strip('[(,)]')
                points = int(point)
                points += fpts
                fpoints = str(points)
                c.execute('INSERT INTO participants (student, act_id) VALUES ("'+session['username']+'", "'+id+'")')
                c.execute('UPDATE tutor_groups SET points = "'+fpoints+'" WHERE id = "'+tutor+'"')
                #c.execute('INSERT INTO participants (student, act_id) VALUES ("'+session['username']+'", "'+id+'"')


                #c.execute('INSERT INTO participants (student, act_id) VALUES (?, ?)', ('hello', 1))
                con.commit()
                con.close()
            else:
                return render_template('noAttend.html', query=query, attendance=attendance)

            return render_template('activitiesAttend.html', query=query, attendance=attendance)


        elif session['role'] == 'tutors' or session['role'] == 'house':
            print(None)
    else:
        print(None)




    return render_template('activities.html', query=query, attendance=attendance)


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            points = int(request.form['points'])

            if not name:
                flash('Name is required!')
            elif not description:
                flash('Description is required!')
            else:
                conn = get_db_connection()
                conn.execute('INSERT INTO activities (name, description, points) VALUES (?, ?, ?)',
                             (name, description, points))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
    return render_template('create.html')

@app.route("/date", methods=['GET', 'POST'])
def date():

    conn = get_db_connection()


    names = conn.execute('SELECT name FROM activities').fetchall()
    conn.close()
    print(names)


    if request.method == 'POST':
            name = request.form['name']
            date = request.form['date']
            time = request.form['time']

            if not name:
                flash('Name is required!')
            elif not date:
                flash('Date is required!')
            elif not time:
                flash('Time is required!')
            else:
                conn = get_db_connection()
                conn.execute('INSERT INTO attendance (name, act_date, act_time) VALUES (?, ?, ?)',
                             (name, date, time))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
    return render_template('date.html', names=names)


@app.route("/record")
def record():
    return render_template('record.html')


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, host='127.0.0.1')


#@app.route("/points")
#def points():
#    conn = get_db_connection()
#    houses = conn.execute('SELECT * FROM houses').fetchall()
#    conn.close()
#    if session.get('username'):
#        print(session['house'])
#        house = ''.join(session['house'][0])
#        print(house)
#        print(type(house))
#        if house == 'Gladius':
#            points = tutor_pts('Gladius')
#        elif house == 'Mitre,':
#            points = tutor_pts('Mitre')
#        elif house == 'Taja,':
#            points = tutor_pts('Taja')
#        elif house == 'Scudo,':
#           points = tutor_pts('Scudo')
#       else:
#            points = tutor_pts('Boek')
#    else:
#        points = 'No Data'

#    print(points)
#    print(houses)
#    return render_template('points.html', houses=houses, points=points)


#def tutor_pts(house):
#    con = sqlite3.connect('zfschool1.db')
#    c = con.cursor()
#    points = c.execute('SELECT id, points FROM tutor_groups WHERE house = "' + house + '"').fetchall()
#    print(points)
#    con.close()
#    return points
