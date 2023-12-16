-- lists all cities of California that can be found in the database hbtn_0d_usa
SELECT id
FROM hbtn_0d_usa.states
WHERE states.name='California'
ORDER BY state_id ASC;
