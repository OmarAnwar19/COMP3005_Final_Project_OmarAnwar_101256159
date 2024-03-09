INSERT INTO Members (username, password, fitness_goal, achievements) VALUES
('JohnDoe', 'password1', 'Lose weight', 'Won State Derby'),
('JaneSmith', 'password2', 'Gain muscle', 'Climbed Everest'),
('RobertJohnson', 'password3', 'Improve stamina', 'Ran 100 miles'),
('MichaelWilliams', 'password', 'Increase flexibility', 'Won National Yoga Competition, Won International Yoga Competition'),
('SarahBrown', 'password5', 'Improve overall fitness', 'Won World Strongman Competition'),
('a', 'a', 'Win the lottery', 'Won the lottery');

INSERT INTO Trainers (username, password, available_from, available_to) VALUES
('TrainerAlex', 'password1', '2022-01-01 09:00:00', '2024-12-31 17:00:00'),
('TrainerBeth', 'password2', '2022-01-01 09:00:00', '2024-12-31 17:00:00'),
('TrainerCharlie', 'password3', '2022-01-01 17:00:00', '2024-12-31 24:00:00'),
('TrainerDiana', 'password4', '2022-01-01 17:00:00', '2024-12-31 00:00:00'),
('TrainerEthan', 'password5', '2022-01-01 00:00:00', '2024-12-31 09:00:00'),
('TrainerKent', 'password6', '2022-01-01 00:00:00', '2024-12-31 09:00:00');

INSERT INTO Administrators (username, password) VALUES
('AdminAlex', 'password1'),
('AdminBeth', 'password2'),
('AdminCharlie', 'password3'),
('AdminDiana', 'password4'),
('AdminEthan', 'password5');

INSERT INTO Rooms (name, booked) VALUES
('Aerobics Arena', TRUE),
('Biceps Bunker', TRUE),
('Cardio Cave', TRUE),
('Dumbbell Den', TRUE),
('Exercise Eden', TRUE),
('Fitness Fortress', FALSE),
('Gymnasium Grotto', FALSE),
('Health Haven', FALSE),
('Iron Inn', FALSE),
('Jogging Jungle', FALSE);

INSERT INTO Equipment (equipment_name, maintenance_due_date) VALUES
('Treadmill Titan', '2022-12-31 00:00:00'),
('Elliptical Eagle', '2022-12-31 00:00:00'),
('Rowing Raptor', '2022-12-31 00:00:00'),
('Bike Bison', '2022-12-31 00:00:00'),
('Weight Wolverine', '2022-12-31 00:00:00');

INSERT INTO Sessions (trainer_id, member_id, room_id, session_time, session_type) VALUES
(1, 1, 1, '2022-12-01 10:00:00', 'Cardio'),
(2, 2, 2, '2022-12-01 11:00:00', 'Pilates'),
(3, 3, 3, '2022-12-01 12:00:00', 'Weights'),
(4, 4, 4, '2022-12-01 13:00:00', 'Yoga'),
(5, 5, 5, '2022-12-01 14:00:00', 'Cross-fit'),
(1, 6, 6, '2022-12-01 15:00:00', 'Cardio');

INSERT INTO Payments (amount, member_id, session_id, payment_time) VALUES
(100, 1, 1, '2022-12-01 10:00:00'),
(200, 2, 2, '2022-12-01 11:00:00'),
(300, 3, 3, '2022-12-01 12:00:00'),
(400, 4, 4, '2022-12-01 14:00:00'),
(500, 5, 5, '2022-12-01 15:00:00'),
(600, 6, 6, '2022-12-01 16:00:00');

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
