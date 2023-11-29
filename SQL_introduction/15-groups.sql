-- script lists # of recors with same score
SELECT score, COUNT(score) as number -- count score count # of same score repetition
FROM second_table
GROUP BY score
ORDER BY score DESC;
