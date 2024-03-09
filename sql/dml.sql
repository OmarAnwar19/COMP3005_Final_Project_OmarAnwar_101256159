INSERT INTO Members (username, password, fitness_goal, achievements) VALUES
('JohnDoe', 'password1', 'Lose weight', 'Won State Derby'),
('JaneSmith', 'password2', 'Gain muscle', 'Climbed Everest'),
('RobertJohnson', 'password3', 'Improve stamina', 'Ran 100 miles'),
('MichaelWilliams', 'password', 'Increase flexibility', 'Won National Yoga Competition, Won International Yoga Competition'),
('SarahBrown', 'password5', 'Improve overall fitness', 'Won World Strongman Competition'),
('MichaelJordan', 'thegoat123', 'Win the lottery', 'Won the lottery');

INSERT INTO Trainers (username, password, available_from, available_to) VALUES
('TrainerAlex', 'password1', '09:00:00', '17:00:00'),
('TrainerBeth', 'password2', '09:00:00', '17:00:00'),
('TrainerCharlie', 'password3', '17:00:00', '24:00:00'),
('TrainerDiana', 'password4', '17:00:00', '00:00:00'),
('TrainerEthan', 'password5', '00:00:00', '09:00:00'),
('TrainerKent', 'password6', '00:00:00', '09:00:00');

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

INSERT INTO Equipment (equipment_name, broken, maintenance_date) VALUES
('Treadmill Titan', TRUE, '2024-12-31'),
('Elliptical Eagle', TRUE, '2024-01-15'),
('Rowing Raptor', FALSE, '2024-02-20'),
('Bike Bison', FALSE, '2024-03-25'),
('Weight Wolverine', FALSE, '2024-04-30');

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
