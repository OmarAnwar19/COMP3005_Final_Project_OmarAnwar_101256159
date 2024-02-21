INSERT INTO Members (username, password, fitness_goal, health_metrics) VALUES
('JohnDoe', 'password1', 'Lose weight', 'BMI: 25'),
('JaneSmith', 'password2', 'Gain muscle', 'BMI: 20'),
('RobertJohnson', 'password3', 'Improve stamina', 'BMI: 22'),
('MichaelWilliams', 'password4', 'Increase flexibility', 'BMI: 24'),
('SarahBrown', 'password5', 'Improve overall fitness', 'BMI: 23');


INSERT INTO Trainers (username, password, availability) VALUES
('Trainer1', 'password1', '2022-12-01 09:00:00'),
('Trainer2', 'password2', '2022-12-01 10:00:00'),
('Trainer3', 'password3', '2022-12-01 11:00:00'),
('Trainer4', 'password4', '2022-12-01 12:00:00'),
('Trainer5', 'password5', '2022-12-01 13:00:00');


INSERT INTO Administrators (username, password) VALUES
('Admin1', 'password1'),
('Admin2', 'password2'),
('Admin3', 'password3'),
('Admin4', 'password4'),
('Admin5', 'password5');


INSERT INTO Sessions (member_id, trainer_id, session_time, session_type) VALUES
(1, 1, '2022-12-01 10:00:00', 'Personal Training'),
(2, 2, '2022-12-01 11:00:00', 'Group Fitness'),
(3, 3, '2022-12-01 12:00:00', 'Personal Training'),
(4, 4, '2022-12-01 13:00:00', 'Group Fitness'),
(5, 5, '2022-12-01 14:00:00', 'Personal Training');


INSERT INTO Rooms (room_name, booking_time) VALUES
('Room 1', '2022-12-01 10:00:00'),
('Room 2', '2022-12-01 11:00:00'),
('Room 3', '2022-12-01 12:00:00'),
('Room 4', '2022-12-01 13:00:00'),
('Room 5', '2022-12-01 14:00:00');


INSERT INTO Equipment (equipment_name, maintenance_due_date) VALUES
('Treadmill 1', '2022-12-31 00:00:00'),
('Elliptical 1', '2022-12-31 00:00:00'),
('Rowing Machine 1', '2022-12-31 00:00:00'),
('Exercise Bike 1', '2022-12-31 00:00:00'),
('Weight Machine 1', '2022-12-31 00:00:00');


INSERT INTO Payments (member_id, amount, payment_time) VALUES
(1, 50.00, '2022-12-01 11:00:00'),
(2, 60.00, '2022-12-01 12:00:00'),
(3, 70.00, '2022-12-01 13:00:00'),
(4, 80.00, '2022-12-01 14:00:00'),
(5, 90.00, '2022-12-01 15:00:00');