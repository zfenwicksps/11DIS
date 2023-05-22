import sqlite3
import json
import requests

from flask import Flask, render_template, request, url_for, flash, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = 'mysupersecretkey'

#url = "https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s=daft_punk"
#url = "https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s=daft_punk&a=Homework"
#url = "https://theaudiodb.com/api/v1/json/523532/search.php?s=coldplay"
album = "https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s=daft_punk"


def get_db_connection():
    conn = sqlite3.connect('northsidedj.db')
    conn.row_factory = sqlite3.Row  # Way of returning sql data
    return conn


############# HOME #############

@app.route("/")
@app.route("/index")
def index():
    if session.get('username'):
        return render_template('index.html')
    else:
        flash('Please Login First')
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('id', None)

    return redirect(url_for('index'))


############# REGISTER #############

@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    elif request.method == "GET":
        return render_template("register.html")
    else:
        #email = request.form['email']
        #print(email)
        #print(type(email))
        #con = sqlite3.connect('northsidedj.db')
        #c = con.cursor()
        #exists = c.execute('SELECT email FROM users WHERE "'+email+'"').fetchall()
        #c.close()
        #print(exists)

        user_details = (
            request.form['fname'], # get data from form
            request.form['lname'],
            request.form['email'],
            request.form['password'],
            False
        )

        insertuser(user_details) # call function using user_detail data
        session['username'] = request.form['email']
### may need session variable and flash success
        return render_template("registersuccess.html")

## function to input a user into the database
def insertuser(user_details):
    con = sqlite3.connect('northsidedj.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    dj BOOLEAN NOT NULL,
    DJ_type TEXT)''')
    sql_execute_string = 'INSERT INTO users (fname, lname, email, password, DJ) VALUES (?, ?, ?, ?, ?)'
    c.execute(sql_execute_string, user_details)
    con.commit()
    con.close()


############# LOGIN #############

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    elif request.method == 'POST':
        con = sqlite3.connect('northsidedj.db')
        c = con.cursor()

        email = request.form['email']
        password = request.form['password']


        results = c.execute(
            'SELECT email, password FROM users where email= "' + email + '" AND password= "' + password + '" ').fetchall()


        #results = stuff.fetchall()

        if len(results) == 0:
            return render_template("unsuccessful.html")
        # Incorrect username or password
        else:

            session['username'] = email


            return render_template("loginsuccess.html")

    return render_template("login.html")


############# JOIN EVENT ############

@app.route("/joinevent", methods=['GET', 'POST'])
def joinevent():
    if request.method == 'POST':

        id = request.form['code']
        session['id'] = id
        con = sqlite3.connect('northsidedj.db')
        c = con.cursor()
        code = c.execute('SELECT code FROM events WHERE code = "'+id+'"')


        for c in code:
            string = str(c)
            s = string.strip('(,)')
        con.close()
        con = sqlite3.connect('northsidedj.db')
        c = con.cursor()
        u = c.execute('SELECT attendees FROM events WHERE code = "'+id+'"')


        for i in u:

            if str(i) == '(None,)':
                user = c.execute('SELECT id FROM users WHERE email = "'+session['username']+'"')
                for use in user:
                    usre = str(use)
                    usre = usre.strip('(,)')


                c.execute('UPDATE events SET attendees = "'+usre+'" WHERE code = "'+s+'"')
            else:
                user = c.execute('SELECT id FROM users WHERE email = "'+session['username']+'"')
                for use in user:
                    usre = str(use)
                    usre = usre.strip('(,)')
                attendees = c.execute('SELECT attendees FROM events WHERE code = "'+s+'"')
                new_attendees = []
                for a in attendees:
                    a = str(a)
                    #print(a)        ###  The following code strips each number already from the database of
                    a = a.split(',') ###  this ensures that when the items are updated with the new user's id
                    for item in a:   ###  that it remains in the same formatting.
                        item = item.strip('("[]",')
                        item = item.strip("''")
                        item = item.strip(" '")
                        if item == usre:
                            break
                        elif item != ')':
                            new_attendees.append(item)



                new_attendees.append(usre)
                new_attendees = str(new_attendees)
                #print(new_attendees)
                c.execute('UPDATE events SET attendees = "'+new_attendees+'" WHERE code = "'+s+'"')
        con.commit()
        con.close()

        #print(u)

        if id == s:
            #attendee = f'UPDATE events SET attendees = {user} WHERE code = {s}'


            #c.execute(attendee)
            return redirect(url_for('event'))
        else:
            flash('Incorrect Code. Try Again')



    return render_template('joinevent.html')


############# EVENT #############

@app.route("/event", methods=['GET', 'POST', 'do'])
def event():
    if request.method == 'POST':
        #print(1)
        artist_name = request.form['artist']
        #albums = search_albums(artist_name)
        #session['artist'] = artist_name

        req = requests.get("https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s='"+artist_name+"'")
        print(req)
        source = req.text
        print(source)
        data = json.loads(source)
        print(data)
        #print(data)
        #print(data.keys())
        mydata = data['album']
        #print(mydata)
        #print(mydata)
        albums = []
        print(mydata)
        print(type(mydata))
        if mydata == None:
            albums = f'No albums listed for { artist_name }'
        else:
            for item in mydata:
                albums.append(item['idAlbum'])
        #print(albums)
        all_tracks = []
        for item in albums:
            tracks = f"https://theaudiodb.com/api/v1/json/523532/track.php?m={item}"
            req1 = requests.get(tracks)
            source1 = req1.text
            data1 = json.loads(source1)
            mydata1 = data1['track']
            #print(mydata1)
            for track in mydata1:
                #print(track)

                all_tracks.append(track['strTrack'])
                t = int(track['idTrack'])
                song = (
                        t,
                        track['strTrack'],
                        track['idAlbum'],
                        track['idArtist']
                )
                con = sqlite3.connect('northsidedj.db')
                c = con.cursor()
                art = c.execute('SELECT artist FROM songs WHERE artist = "'+track['idArtist']+'"')
                #print(art)
                list = []
                for a in art:
                    list.append(a)
                #print(type([]))
                con.close()
                if list == []:
                    con = sqlite3.connect('northsidedj.db')
                    c = con.cursor()
                    c.execute('''CREATE TABLE IF NOT EXISTS songs
                    (id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    album TEXT NOT NULL,
                    artist TEXT NOT NULL)''')
                    sql_execute_string = 'INSERT INTO songs (id, name, album, artist) VALUES (?, ?, ?, ?)'
                    c.execute(sql_execute_string, song)
                    con.commit()
                    con.close()



        #print(all_tracks)
        session['artist_name'] = artist_name
        session['albums'] = albums
        session['tracks'] = all_tracks
        #print(albums)
        #print(all_tracks)



        return redirect(url_for('search'))
    else:



        return render_template('event.html')





@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

        track = request.form['track']
        con = sqlite3.connect('northsidedj.db')
        c = con.cursor()
        other = c.execute('SELECT v_count FROM queue WHERE song_id = "'+track+'"')
        o = 0
        for o in other:
            o = str(o)
            o = o.strip("('',)")
            o = int(o)
        o += 1
        if o == 1:
            #o = int(o)
            #print(o)

            queue = (
                            session['id'],
                            track,
                            +1
            )

            con = sqlite3.connect('northsidedj.db')
            c = con.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS queue
            (event_id INTEGER NOT NULL,
            song_id INTEGER NOT NULL,
            v_count TEXT NOT NULL,
    
            FOREIGN KEY (event_id) REFERENCES events(code),
            FOREIGN KEY (song_id) REFERENCES songs(name))''')
            sql_execute_string = 'INSERT INTO queue (event_id, song_id, v_count) VALUES (?, ?, ?)'
            c.execute(sql_execute_string, queue)
            con.commit()
            con.close()
        else:
            o = str(o)
            print(o)
            con = sqlite3.connect('northsidedj.db')
            c = con.cursor()
            c.execute('UPDATE queue SET v_count = "'+o+'" WHERE song_id = "'+track+'"')
            con.commit()
            con.close()

   ########## save_albums_to_db(session['artist'], albums)



    #print(data)
    #print(data.keys())
  #  print(type(mydata))

    return render_template('search.html', artist=session['artist_name'], albums=session['albums'], tracks=session['tracks'])









def search_albums(artist_name):
    API_KEY = '523532'
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    response = requests.get(URL)
    data = response.json()
    albums = data['album']
    return albums


def save_albums_to_db(artist_name, albums):
    conn = sqlite3.connect('northsidedj.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS songs
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        album TEXT NOT NULL,
        artist TEXT NOT NULL)''')

    for album in albums:
        print(album['idAlbum'])
        c.execute("INSERT INTO songs VALUES (?,?,?,?)", (album['idTrack'], album['strTrack'], album['idAlbum'], artist_name))
    conn.commit()
    conn.close()


########## BOOK DJ ###########

@app.route("/bookDJ", methods=['GET', 'POST'])
def bookDJ():
    #print(1)
    #print(session.get('username'))
    if session.get('username'):
        dj = []
        if request.method == 'POST':
            if request.form.get('rave') == 'rave':           # the following 'if' statements are kept as 'if' rather than 'elif'
                dj.append('rave')                            # because if it were to be 'elif' the following checkboxes
            if request.form.get('club') == 'club':           # would be skipped
                dj.append('club')
            if request.form.get('wedding') == 'wedding':
                dj.append('wedding')
            if request.form.get('formal') == 'formal':
                dj.append('formal')
            if request.form.get('party') == 'party':
                dj.append('party')
            dj = str(dj) #convert to string
            dj_type = dj.strip("[']") #strip brackets and '
            #print(dj_type)
            con = sqlite3.connect('northsidedj.db')

            #c = con.cursor()
            #conn = get_db_connection()
            c = con.cursor()
            c.execute("SELECT * FROM events WHERE dj_type = '"+dj_type+"' AND event_date = '"+request.form.get('date')+"' ")
            events = c.fetchall()
            print(events)
            for e in events:
                if e[2] == request.form.get('start') or e[3] == request.form.get('end'):
                    flash("Sorry but there are no DJs that can perform at this event")
                    flash("Please change the event date, start/end time or dj type")
                    break


            con = sqlite3.connect('northsidedj.db')
            c = con.cursor()
            sql_email = "SELECT * FROM users WHERE DJ_type = '"+dj_type+"'"

            #c.execute('SELECT email FROM users WHERE DJ_type = "rave"') #Get DJ email that equals DJ type selected
            c.execute(sql_email)
            events = c.fetchall()

            for e in events:
                email = e[3]


                #e = email[0]
                #print(f'{e.keys()=}')
                #for k in e.keys():
                #    print(f'{k=}')
                #print(f'{e.keys()=email}')
                c.close()
                #print(request.form.get('start')) # data provided in the form 21:30
                #print(request.form.get('end')) # data provided in the form 00:00
                #print(request.form.get('date')) # data provided in the form 2023-05-13

            event_details = (
                request.form.get('date'), # get data from form
                request.form.get('start'),
                request.form.get('end'),
                request.form.get('address'),
                email,
                dj_type
            )
            #print(event_details)
            #print(request.form.get('address'))
            #print(type(request.form.get('address')))
            con = sqlite3.connect('northsidedj.db')
            c = con.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS events
            (code INTEGER PRIMARY KEY AUTOINCREMENT,
            event_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            location TEXT NOT NULL,
            dj_email TEXT NOT NULL,
            dj_type TEXT NOT NULL,
            attendees TEXT)''')
            sql_execute_string = 'INSERT INTO events (event_date, start_time, end_time, location, dj_email, dj_type) VALUES (?, ?, ?, ?, ?, ?)'
            c.execute(sql_execute_string, event_details)
            con.commit()

            con.close()
            flash(f"You event has been created for {request.form.get('date')}, starting at {request.form.get('start')}, ending at {request.form.get('end')}  ")


        return render_template('bookDJ.html')
    else:
        flash('Please Login First')
        return redirect(url_for('login'))






@app.route("/friends")
def friends():
    #print(session.get('username'))
    if session.get('username'):
        return render_template('friends.html')
    else:
        flash('Please Login First')
        return redirect(url_for('login'))


@app.route("/queue", methods=['GET', 'POST'])
def queue():
    if session.get('id'):
        if request.method == 'POST':
            con = sqlite3.connect('northsidedj.db')
            c = con.cursor()
            if request.form.get('order') == "a-z":
                queue = c.execute('SELECT song_id FROM queue WHERE event_id = "'+session['id']+'" ORDER BY song_id ASC')
            elif request.form.get('order') == "z-a":
                queue = c.execute('SELECT song_id FROM queue WHERE event_id = "'+session['id']+'" ORDER BY song_id DESC')
            elif request.form.get('order') == "hvotes":
                queue = c.execute('SELECT song_id FROM queue WHERE event_id = "'+session['id']+'" ORDER BY v_count DESC')
            elif request.form.get('order') == "lvotes":
                queue = c.execute('SELECT song_id FROM queue WHERE event_id = "'+session['id']+'" ORDER BY v_count ASC')
            list = []
            for q in queue:
                q = str(q)
                q = q.strip("('',)")
                list.append(q)
        else:
            con = sqlite3.connect('northsidedj.db')
            c = con.cursor()
            queue = c.execute('SELECT song_id FROM queue WHERE event_id = "'+session['id']+'" ORDER BY v_count ASC')
            list = []
            for q in queue:
                q = str(q)
                q = q.strip("('',)")
                list.append(q)
            #songs = []
            #votes = []
            #both = []
            #for q in queue:
            #    both.append(list(q))
            #    songs.append(str(q[0]))
            #    votes.append(str(q[1]))
            #b = both[0]
            #print(b[0])
            #print(both)
        return render_template('queue.html', queue=list)
    else:
        flash('Please Join an Event First')
        return render_template('queue.html')





if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, host='127.0.0.1')
