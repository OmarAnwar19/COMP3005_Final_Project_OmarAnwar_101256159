INSERT INTO Members (username, password, fitness_goal, health_metrics) VALUES
('JohnDoe', 'password1', 'Lose weight', 'BMI: 25'),
('JaneSmith', 'password2', 'Gain muscle', 'BMI: 20'),
('RobertJohnson', 'password3', 'Improve stamina', 'BMI: 22'),
('MichaelWilliams', 'password', 'Increase flexibility', 'BMI: 24'),
('SarahBrown', 'password5', 'Improve overall fitness', 'BMI: 23');

INSERT INTO Trainers (username, password, available) VALUES
('FitFrank', 'password1', TRUE),
('MuscleMary', 'password2', TRUE),
('StaminaSteve', 'password3', FALSE),
('FlexibilityFiona', 'password4', TRUE),
('OverallOscar', 'password5', FALSE);

INSERT INTO Administrators (username, password) VALUES
('AdminAlex', 'password1'),
('AdminBeth', 'password2'),
('AdminCharlie', 'password3'),
('AdminDiana', 'password4'),
('AdminEthan', 'password5');

INSERT INTO Rooms (room_name, booking_time) VALUES
('Aerobics Arena', '2022-12-01 10:00:00'),
('Biceps Bunker', '2022-12-01 11:00:00'),
('Cardio Cave', '2022-12-01 12:00:00'),
('Dumbbell Den', '2022-12-01 13:00:00'),
('Exercise Eden', '2022-12-01 14:00:00');

INSERT INTO Equipment (equipment_name, maintenance_due_date) VALUES
('Treadmill Titan', '2022-12-31 00:00:00'),
('Elliptical Eagle', '2022-12-31 00:00:00'),
('Rowing Raptor', '2022-12-31 00:00:00'),
('Bike Bison', '2022-12-31 00:00:00'),
('Weight Wolverine', '2022-12-31 00:00:00');

INSERT INTO Sessions (id, trainer_id, session_time, session_type) VALUES
(1, 1, '2022-12-01 10:00:00', 'Personal Training'),
(2, 2, '2022-12-01 11:00:00', 'Group Fitness'),
(3, 3, '2022-12-01 12:00:00', 'Personal Training'),
(4, 4, '2022-12-01 13:00:00', 'Group Fitness'),
(5, 5, '2022-12-01 14:00:00', 'Personal Training');

INSERT INTO Payments (id, amount, payment_time) VALUES
(1, 50.00, '2022-12-01 11:00:00'),
(2, 60.00, '2022-12-01 12:00:00'),
(3, 70.00, '2022-12-01 13:00:00'),
(4, 80.00, '2022-12-01 14:00:00'),
(5, 90.00, '2022-12-01 15:00:00');

INSERT INTO Exercises (id, exercise_name, exercise_time) VALUES
(1, 'Cardio', '2022-12-01 10:00:00'),
(2, 'Cross-fit', '2022-12-01 11:00:00'),
(3, 'Pilates', '2022-12-01 12:00:00'),
(4, 'Cardio', '2022-12-01 13:00:00'),
(5, 'Cardio', '2022-12-01 14:00:00');

INSERT INTO Achievements (id, achievement_name, achievement_date) VALUES
(1, '5k Run', '2022-12-01'),
(2, '10k Run', '2022-12-01'),
(3, 'Half Marathon', '2022-12-01'),
(4, 'Marathon', '2022-12-01'),
(5, 'Triathlon', '2022-12-01');

INSERT INTO HealthStats (id, workouts_completed, sessions_booked, calories_burned, stat_date) VALUES
(1, 10, 5, 500, '2022-12-01'),
(2, 20, 10, 1000, '2022-12-01'),
(3, 30, 15, 1500, '2022-12-01'),
(4, 40, 20, 2000, '2022-12-01'),
(5, 50, 25, 2500, '2022-12-01');