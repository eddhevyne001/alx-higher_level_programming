-- Lists the number of records with the same score
-- in MySQL Server.

SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
