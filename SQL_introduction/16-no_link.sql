-- script lists all records
SELECT score, name 
FROM second_table
WHERE score IS NOT NULL
ORDER BY score DESC;
