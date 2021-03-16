CREATE TABLE  users (
   	user_id VARCHAR PRIMARY KEY,
	first_name VARCHAR ( 50 ) UNIQUE NOT NULL,
	last_name VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	user_name VARCHAR ( 50 ) UNIQUE NOT NULL,
	password BYTEA NOT NULL
);
