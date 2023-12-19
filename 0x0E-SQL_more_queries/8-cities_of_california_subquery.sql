-- Script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa
-- database name will be passed as an argument of mysql command
SELECT * FROM cities WHERE id = (
	SELECT id FROM states WHERE name = 'California'
);
