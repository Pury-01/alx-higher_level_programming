-- creates the mysql server user user_0d_1
-- user has all privileges

CREATE USER IF NOT EXISTS 'user_0d_01'@'localhost' IDENTIFIIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
