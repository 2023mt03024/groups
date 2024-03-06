DROP TABLE IF EXISTS groups;

CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    member1 TEXT,
    member2 TEXT,
    member3 TEXT,
    member4 TEXT,
    member5 TEXT
);

