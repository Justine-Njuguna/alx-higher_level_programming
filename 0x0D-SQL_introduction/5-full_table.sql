-- Print the full description of the table

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM information_schema.columns
WHERE TABLE_SCHEMA = '$1' AND TABLE_NAME = 'first_table';

