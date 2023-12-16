-- creates db and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usañ
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL FOREIGN KEY references states(id)
    name VARCHAR(256) NOT NULL);
