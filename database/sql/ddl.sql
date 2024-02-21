CREATE TABLE IF NOT EXISTS Members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    fitness_goal VARCHAR(100),
    health_metrics VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Trainers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS Administrators (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Sessions (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    trainer_id INTEGER REFERENCES Trainers(id),
    session_time TIMESTAMPTZ NOT NULL,
    session_type VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Rooms (
    id SERIAL PRIMARY KEY,
    room_name VARCHAR(50) NOT NULL,
    booking_time TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS Equipment (
    id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(50) NOT NULL,
    maintenance_due_date TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS Payments (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_time TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS Exercises (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    exercise_name VARCHAR(50) NOT NULL,
    exercise_time TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS Achievements (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    achievement_name VARCHAR(50) NOT NULL,
    achievement_date TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS HealthStats (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(id),
    stat_name VARCHAR(50) NOT NULL,
    stat_value VARCHAR(50) NOT NULL,
    stat_date TIMESTAMPTZ NOT NULL
);