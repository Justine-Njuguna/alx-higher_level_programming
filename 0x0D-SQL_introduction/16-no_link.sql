-- List all records with a name value from the second_table
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
