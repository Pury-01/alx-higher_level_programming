-- creates hbtn_0d_2 database and user user_0d_2
-- password set to user_0d_2_pwd

CREATE DATABASE IIF NoT EXISTS hbtn_0d_2;
CREATE USER IF NoT ExISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
