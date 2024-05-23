-- lists all records of the table second_table of htbn_0c_0

SELECT score, name FROM second_table HAVING name is NOT NULL
ORDERED BY score DESC;
