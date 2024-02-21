CREATE TABLE Members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    fitness_goal VARCHAR(100),
    health_metrics VARCHAR(100)
);


CREATE TABLE Trainers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    availability TIMESTAMPTZ
);


CREATE TABLE Administrators (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);


CREATE TABLE Sessions (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES members(id),
    trainer_id INTEGER REFERENCES trainers(id),
    session_time TIMESTAMPTZ NOT NULL,
    session_type VARCHAR(50) NOT NULL
);


CREATE TABLE Rooms (
    id SERIAL PRIMARY KEY,
    room_name VARCHAR(50) NOT NULL,
    booking_time TIMESTAMPTZ
);


CREATE TABLE Equipment (
    id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(50) NOT NULL,
    maintenance_due_date TIMESTAMPTZ
);


CREATE TABLE Payments (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES members(id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_time TIMESTAMPTZ NOT NULL
);