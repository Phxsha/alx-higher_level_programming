-- Prints full description of a specitfied table in a database
-- Print full description of first_table
SELECT TABLE_NAME, CREATE_TABLE
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

