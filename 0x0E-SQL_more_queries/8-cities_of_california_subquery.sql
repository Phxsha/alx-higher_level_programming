-- Script to list all cities of California in the database hbtn_0d_usa

-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- Retrieve the id of California
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- Select cities of California using subquery
SELECT * FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;

