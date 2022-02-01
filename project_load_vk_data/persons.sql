CREATE TABLE IF NOT EXISTS persons (
    id INTEGER,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    is_closed BOOLEAN,
    sex INTEGER,
    bdate DATE,
    city VARCHAR(128)
);