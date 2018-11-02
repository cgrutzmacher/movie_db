DROP DATABASE IF EXISTS bmdb;
CREATE DATABASE bmdb;
USE bmdb;


CREATE TABLE movie ( 
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    TITLE				VARCHAR(100)	NOT NULL,
    GENRE				INT				NOT NULL,
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
    firstName			VARCHAR(25)		NOT NULL,
    lastName			VARCHAR(25)		NOT NULL,
    gender				VARCHAR(6)		NOT NULL,	
    birthday			DATE			NOT NULL    
);

CREATE TABLE movieGenre (
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    movieID				INT				NOT NULL,
    genreID				INT				NOT NULL,    
    FOREIGN KEY (movieID) REFERENCES movie (ID),
    FOREIGN KEY (genreID) REFERENCES genre (ID)
);

CREATE TABLE credit ( 
	ID					INT				PRIMARY KEY		AUTO_INCREMENT,
    movieID				INT,
    actorID				INT,
    characterName		VARCHAR(50),
    FOREIGN KEY (movieID) REFERENCES movie (ID),
    FOREIGN KEY (actorID) REFERENCES artist (ID)
);

CREATE USER IF NOT EXISTS 'python_connector'@'localhost' IDENTIFIED BY 'sudo';
GRANT ALL PRIVILEGES ON bmdb.*
TO 'python_connector'@'localhost';



