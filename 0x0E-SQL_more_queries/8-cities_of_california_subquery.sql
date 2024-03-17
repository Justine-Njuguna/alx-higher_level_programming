-- Task 8: List cities of California without using JOIN

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Retrieve the state_id for California from the states table
SET @california_state_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California using the retrieved state_id
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id ASC;
