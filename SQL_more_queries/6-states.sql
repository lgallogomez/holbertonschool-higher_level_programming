-- creates database and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL UNIQUE PRIMARY KEY, 
    name VARCHAR(256) NOT NULL
);