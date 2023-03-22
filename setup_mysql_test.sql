-- Create a MYSQL server for the project
-- Create a database with the name: hbnb_test_dB
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a user and a password for the server
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Give privileges to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
