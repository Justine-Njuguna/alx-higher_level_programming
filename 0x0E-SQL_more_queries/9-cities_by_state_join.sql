-- Task 9: List all cities with corresponding states

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List all cities with corresponding states and sort by cities.id
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
