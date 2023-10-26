-- Create the database
CREATE DATABASE gnosis;

-- Create the user role
CREATE ROLE atlas WITH LOGIN PASSWORD 'password';

-- Grant the user full privileges on the database
GRANT ALL PRIVILEGES ON DATABASE gnosis TO atlas;
