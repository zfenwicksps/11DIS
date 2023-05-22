DROP TABLE IF EXISTS student;
CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    DOB TEXT NOT NULL,
    gender TEXT NOT NULL,
    std_pts INTEGER,
    house TEXT NOT NULL,
    tutor_id TEXT NOT NULL,
    FOREIGN KEY (house) REFERENCES houses(name)
    FOREIGN KEY (tutor_id) REFERENCES tutor_groups(id)
);


DROP TABLE IF EXISTS tutors;
CREATE TABLE tutors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    DOB TEXT NOT NULL,
    gender TEXT NOT NULL,
    house TEXT NOT NULL,
    tutor_id INTEGER,
    FOREIGN KEY (house) REFERENCES houses(name),
    FOREIGN KEY (tutor_id) REFERENCES tutor_groups(id)
);


DROP TABLE IF EXISTS tutor_groups;
CREATE TABLE tutor_groups (
    id TEXT PRIMARY KEY,
    room TEXT,
    teacher TEXT,
    house TEXT NOT NULL,
    points INTEGER NOT NULL,
    FOREIGN KEY (house) REFERENCES houses(name)
);

DROP TABLE IF EXISTS houses;
CREATE TABLE houses (
    name TEXT NOT NULL PRIMARY KEY,
    house_leader TEXT NOT NULL,
    points INTEGER
);

DROP TABLE IF EXISTS activities;
CREATE TABLE activities (
    name TEXT NOT NULL PRIMARY KEY,
    description TEXT NOT NULL,
    points INTEGER
);

DROP TABLE IF EXISTS attendance;
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    act_date TEXT NOT NULL,
    act_time TEXT NOT NULL,
    students TEXT,
    FOREIGN KEY (name) REFERENCES activities(name)
);


DROP TABLE IF EXISTS attendance;
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    act_date TEXT NOT NULL,
    act_time TEXT NOT NULL,
    students TEXT,
    FOREIGN KEY (name) REFERENCES activities(name)
);

DROP TABLE IF EXISTS participants;
CREATE TABLE participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT NOT NULL,
    act_id TEXT NOT NULL,
    FOREIGN KEY (act_id) REFERENCES attendance(id)
);
