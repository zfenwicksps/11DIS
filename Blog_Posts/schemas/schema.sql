DROP TABLE IF EXISTS student;

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT NOT NULL,
    DOB TEXT NOT NULL,
    gender TEXT NOT NULL,
    std_pts INTEGER NOT NULL,
    tutor_id INTEGER NOT NULL
);
