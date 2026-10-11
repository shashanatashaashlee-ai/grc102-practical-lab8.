CREATE DATABASE IF NOT EXISTS customer_data;
USE customer_data;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    ssn VARCHAR(20),
    date_of_birth DATE,
    address VARCHAR(255),
    credit_card VARCHAR(30)
);

INSERT INTO customers
    (first_name, last_name, email, ssn, date_of_birth, address, credit_card)
VALUES
    ('Test', 'Customer1', 'customer1@example.test', '000-00-0001',
     '1990-01-01', 'Synthetic Address 1', '0000000000000001'),
    ('Test', 'Customer2', 'customer2@example.test', '000-00-0002',
     '1985-05-15', 'Synthetic Address 2', '0000000000000002');
