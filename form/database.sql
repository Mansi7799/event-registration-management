CREATE DATABASE eventdb;

USE eventdb;

CREATE TABLE registrations (
    id INT auto_increment KEY,
    fullname VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    event_name VARCHAR(100),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

