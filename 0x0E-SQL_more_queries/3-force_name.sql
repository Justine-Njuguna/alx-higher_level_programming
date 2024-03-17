-- Task 3: Create table force_name

-- Create table force_name if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
