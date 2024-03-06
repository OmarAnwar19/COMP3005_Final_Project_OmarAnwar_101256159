INSERT INTO Members (username, password, fitness_goal, achievements) VALUES
('JohnDoe', 'password1', 'Lose weight', 'Won State Derby'),
('JaneSmith', 'password2', 'Gain muscle', 'Climbed Everest'),
('RobertJohnson', 'password3', 'Improve stamina', 'Ran 100 miles'),
('MichaelWilliams', 'password', 'Increase flexibility', 'Won National Yoga Competition, Won International Yoga Competition'),
('SarahBrown', 'password5', 'Improve overall fitness', 'Won World Strongman Competition'),
('a', 'a', 'Win the lottery', 'Won the lottery');

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

INSERT INTO Sessions (trainer_id, session_time, session_type) VALUES
(1, '2022-12-01 10:00:00', 'Personal Training'),
(2, '2022-12-01 11:00:00', 'Group Fitness'),
(3, '2022-12-01 12:00:00', 'Personal Training'),
(4, '2022-12-01 13:00:00', 'Group Fitness'),
(5, '2022-12-01 14:00:00', 'Personal Training');

INSERT INTO Payments (amount) VALUES
(50.00),
(60.00),
(70.00),
(80.00),
(90.00);

INSERT INTO Exercises (member_id, exercise_name) VALUES
(1, 'Cardio'),
(2, 'Pilates'),
(3, 'Weights'),
(4, 'Yoga'),
(5, 'Yoga'),
(6, 'Cross-fit');

INSERT INTO HealthStats (member_id, weight_lbs, heart_rate, sleep_hours) VALUES
(1, 150, 70, 8),
(2, 160, 72, 7),
(3, 155, 68, 8),
(4, 170, 75, 6),
(5, 180, 70, 7),
(6, 285, 80, 5);
