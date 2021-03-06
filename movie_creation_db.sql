DROP DATABASE IF EXISTS bmdb;
CREATE DATABASE bmdb;
USE bmdb;


CREATE TABLE movie ( 
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    TITLE				VARCHAR(100)	NOT NULL		UNIQUE,
    GENRE				VARCHAR(20)		NOT NULL,
    RATING				VARCHAR(5)		NOT NULL,
    `YEAR`				INT				NOT NULL,
    DIRECTOR			VARCHAR(50)		NOT NULL

);

CREATE TABLE genre ( 
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    genreTitle			VARCHAR(12)		NOT NULL
);

CREATE TABLE artist ( 
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    artistName			VARCHAR(50)		NOT NULL		UNIQUE   
);


CREATE TABLE credit ( 
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    movieID				INT,
    actorID				INT,
    FOREIGN KEY (movieID) REFERENCES movie (ID),
    FOREIGN KEY (actorID) REFERENCES artist (ID)
);

CREATE USER IF NOT EXISTS 'python_connector'@'localhost' IDENTIFIED BY 'sudo';
GRANT ALL PRIVILEGES ON bmdb.*
TO 'python_connector'@'localhost';



