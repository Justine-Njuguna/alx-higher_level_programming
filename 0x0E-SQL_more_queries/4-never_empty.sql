-- Task 4: Create table id_not_null

-- Create table id_not_null if it doesn't already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
