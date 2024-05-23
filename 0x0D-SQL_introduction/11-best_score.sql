-- lists all records with a score >= 10 in second_table
-- of database hbtn_0c_0 in mysql server
-- results dispaly both the score and the name
-- Records are ordered by score (top first)

SELECT score, name FROM second_table WHERE score >= 10 ORDERED BY score DESC;
