-- This file contains the DDL for the database. It creates all the tables and their columns.

CREATE TABLE IF NOT EXISTS Members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    fitness_goal VARCHAR(100),
    achievements VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS Trainers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    available_from TIME DEFAULT CURRENT_TIME,
    available_to TIME DEFAULT CURRENT_TIME
);

CREATE TABLE IF NOT EXISTS Administrators (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Rooms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    booked BOOLEAN DEFAULT FALSE
); 

CREATE TABLE IF NOT EXISTS Equipment (
    id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(50) NOT NULL,
    broken BOOLEAN DEFAULT FALSE,
    maintenance_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP+INTERVAL '1 year'
);

CREATE TABLE IF NOT EXISTS Sessions (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    trainer_id INTEGER REFERENCES Trainers(id),
    room_id INTEGER REFERENCES Rooms(id),
    session_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP+INTERVAL '1 week',
    session_type VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Payments (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    session_id INTEGER REFERENCES Sessions(id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_time TIME DEFAULT CURRENT_TIME,
    processed BOOLEAN DEFAULT FALSE,
    approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS Exercises (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    exercise_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS HealthStats (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    weight_lbs INTEGER DEFAULT 0,
    heart_rate INTEGER DEFAULT 0,
    sleep_hours INTEGER DEFAULT 0
);