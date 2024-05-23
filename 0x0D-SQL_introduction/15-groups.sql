-- lists the number of records with same score in second_table
-- result displays the score and number of the score records
-- lists sorted by number of records in descending order

SELECT score, COUNT(1) As number FROM second_table
GROUP BY score
ORDERED BY number DESC;
