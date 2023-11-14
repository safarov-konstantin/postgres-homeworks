CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(150),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(150),
	contact_name varchar(150)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(10) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(150)
);