-- script lists all records
SELECT score, name 
FROM second_table
GROUP BY name
ORDER BY score DESC;
