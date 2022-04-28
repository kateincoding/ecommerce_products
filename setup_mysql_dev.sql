-- script that prepares a MySQL server fot the dev project

CREATE DATABASE IF NOT EXISTS bsale_test;
CREATE USER IF NOT EXISTS 'bsale_test'@'localhost' IDENTIFIED BY 'bsale_test';
GRANT ALL PRIVILEGES ON bsale_test.* TO 'bsale_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'bsale_test'@'localhost';
FLUSH PRIVILEGES;
