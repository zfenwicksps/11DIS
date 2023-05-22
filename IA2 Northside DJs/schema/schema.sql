DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    dj BOOLEAN NOT NULL,
    DJ_type TEXT
);

DROP TABLE IF EXISTS events;
CREATE TABLE events (
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    event_date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    location TEXT NOT NULL,
    dj_email INTEGER NOT NULL,
    dj_type TEXT NOT NULL,
    attendees TEXT
);

DROP TABLE IF EXISTS songs;
CREATE TABLE songs (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    album TEXT NOT NULL,
    artist TEXT NOT NULL
);

DROP TABLE IF EXISTS queue;
CREATE TABLE queue (
    event_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    v_count TEXT NOT NULL,

    FOREIGN KEY (event_id) REFERENCES events(code),
    FOREIGN KEY (song_id) REFERENCES songs(name)
);


DROP TABLE IF EXISTS favourties;
CREATE TABLE favourties (
    song_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    status TEXT NOT NULL,

    FOREIGN KEY (song_id) REFERENCES songs(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
