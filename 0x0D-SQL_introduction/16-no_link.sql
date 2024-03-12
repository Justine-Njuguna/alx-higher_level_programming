-- List all records with a name value from the second_table
SELECT `score`, name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
