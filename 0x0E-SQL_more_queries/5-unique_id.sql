-- Script to create table unique_id on MySQL server

-- Create table unique_id if not exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

