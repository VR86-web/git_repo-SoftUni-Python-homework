INSERT INTO
	students(student_name)
VALUES
	('Mila'),
	('Toni'),
	('Ron');

INSERT INTO
	exams(exam_name)
VALUES
	('Python Advanced'),
	('Python OOP'),
	('PostgreSQL');

INSERT INTO
	study_halls(study_hall_name, exam_id)
VALUES
	('Open Source Hall', 102),
	('Inspiration Hall', 101),
	('Creative Hall', 103),
	('Masterclass Hall', 103),
	('Information Security Hall', 103);;

INSERT INTO
	students_exams
VALUES
	(1, 101),
	(1, 102),
	(2, 101),
	(3, 103),
	(2, 102),
	(2, 103);;