CREATE TABLE IF NOT EXISTS addresses (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
	id SERIAL PRIMARY KEY,
	name VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS clients (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(50) NOT NULL,
	phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS drivers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	age INT NOT NULL,
	rating NUMERIC(2) DEFAULT 5.5,

	CONSTRAINT ck_drivers_age_is_postive
		CHECK (age > 0)
);

CREATE TABLE IF NOT EXISTS cars (
	id SERIAL PRIMARY KEY,
	make VARCHAR(20) NOT NULL,
	model VARCHAR(20),
	year INT NOT NULL DEFAULT 0,
	mileage INT DEFAULT 0,
	condition CHAR(1) NOT NULL,
	category_id INT NOT NULL,

	CONSTRAINT ck_car_year_is_positive
		CHECK (year > 0),
	CONSTRAINT ck_car_mileage_is_positive
		CHECK (mileage > 0),
	CONSTRAINT fk_cars_categories
		FOREIGN KEY (category_id)
		REFERENCES categories(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS courses (
	id SERIAL PRIMARY KEY,
	from_address_id INT NOT NULL,
	start TIMESTAMP NOT NULL,
	bill NUMERIC(10, 2) DEFAULT 10,
	car_id INT NOT NULL,
	client_id INT NOT NULL,

	CONSTRAINT ck_courses_bill_is_positive
		CHECK (bill > 0),

	CONSTRAINT fk_courses_addresses
		FOREIGN KEY (from_address_id)
		REFERENCES addresses(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_courses_cars
		FOREIGN KEY (car_id)
		REFERENCES cars(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_courses_clients
		FOREIGN KEY (client_id)
		REFERENCES clients(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cars_drivers (
	car_id INT NOT NULL,
	driver_id INT NOT NULL,

	CONSTRAINT fk_cars_drivers_cars
		FOREIGN KEY (car_id)
		REFERENCES cars(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_cars_drivers_drivers
		FOREIGN KEY (driver_id)
		REFERENCES drivers(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);