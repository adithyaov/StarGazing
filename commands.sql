DROP TABLE IF EXISTS Award_mpr_stage;
DROP TABLE IF EXISTS Movie_person_role;
DROP TABLE IF EXISTS Genre_movie;
DROP TABLE IF EXISTS Movie_user;
DROP TABLE IF EXISTS Comment_user;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Award;
DROP TABLE IF EXISTS Stage;
DROP TABLE IF EXISTS Movie_edit_history;
DROP TABLE IF EXISTS Comment_edit_history;
DROP TABLE IF EXISTS Comment;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Movie;


CREATE TABLE Person(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(32) NOT NULL,
	last_name VARCHAR(32) NOT NULL,
	dob DATE,
	bio TEXT
);

CREATE TABLE Role(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	role_title VARCHAR(32) NOT NULL,
	role_description TEXT
);

CREATE TABLE User(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(32) NOT NULL,
	email VARCHAR(128) UNIQUE NOT NULL,
	password_hash VARCHAR(64),
	dob DATE
);

CREATE TABLE Movie(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	movie_title VARCHAR(128),
	release_date DATE,
	age_rating INTEGER,
	avg_rating FLOAT DEFAULT 0.0
);

CREATE TABLE Comment(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	content TEXT,
	date_posted DATE,
	upvotes INTEGER DEFAULT 0,
	downvotes INTEGER DEFAULT 0,
	movie_id INTEGER NOT NULL,
	user_id INTEGER,
	FOREIGN KEY (movie_id) REFERENCES Movie(id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE SET NULL
);

CREATE TABLE Genre(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	genre_name VARCHAR(32) UNIQUE NOT NULL,
	genre_description TEXT
);

CREATE TABLE Award(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	award_name VARCHAR(32) UNIQUE NOT NULL,
	award_description TEXT
);

CREATE TABLE Stage(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	stage_name VARCHAR(32) UNIQUE NOT NULL,
	stage_description TEXT
);


CREATE TABLE Movie_person_role(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	person_id INTEGER NOT NULL,
	role_id INTEGER,
	movie_id INTEGER NOT NULL,
	UNIQUE KEY (person_id, role_id, movie_id),
	FOREIGN KEY (person_id) REFERENCES Person(id) ON DELETE CASCADE,
	FOREIGN KEY (movie_id) REFERENCES Movie(id) ON DELETE CASCADE,
	FOREIGN KEY (role_id) REFERENCES Role(id) ON DELETE SET NULL
);

CREATE TABLE Award_mpr_stage(
	award_id INTEGER NOT NULL,
	mpr_id INTEGER NOT NULL,
	stage_id INTEGER NOT NULL,
	won_in DATE NOT NULL,
	PRIMARY KEY (award_id, mpr_id, stage_id),
	FOREIGN KEY (award_id) REFERENCES Award(id) ON DELETE CASCADE,
	FOREIGN KEY (mpr_id) REFERENCES Movie_person_role(id) ON DELETE CASCADE,
	FOREIGN KEY (stage_id) REFERENCES Stage(id) ON DELETE CASCADE
);

CREATE TABLE Genre_movie(
	genre_id INTEGER NOT NULL,
	movie_id INTEGER NOT NULL,
	PRIMARY KEY (genre_id, movie_id),
	FOREIGN KEY (genre_id) REFERENCES Genre(id) ON DELETE CASCADE,
	FOREIGN KEY (movie_id) REFERENCES Movie(id) ON DELETE CASCADE
);

CREATE TABLE Movie_user(
	movie_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	rating INTEGER NOT NULL CHECK(rating <= 5 && rating >= 0),
	PRIMARY KEY (movie_id, user_id),
	FOREIGN KEY (movie_id) REFERENCES Movie(id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE Comment_user(
	comment_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	vote ENUM('up', 'down'),
	PRIMARY KEY (comment_id, user_id),
	FOREIGN KEY (comment_id) REFERENCES Comment(id) ON DELETE CASCADE,
	FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
);


CREATE TABLE Vote_consistancy(
	change_id INTEGER NOT NULL,
	from_table ENUM('Movie', 'Comment') NOT NULL,
	PRIMARY KEY (change_id, from_table)
);


CREATE TABLE Movie_edit_history(
	movie_id INTEGER NOT NULL,
	content TEXT,
 	edit_time TIME,
 	PRIMARY KEY (movie_id, edit_time),
	FOREIGN KEY (movie_id) REFERENCES Movie(id) ON DELETE CASCADE
);

CREATE TABLE Comment_edit_history(
	comment_id INTEGER NOT NULL,
	content TEXT,
 	edit_time TIME,
 	PRIMARY KEY (comment_id, edit_time),
	FOREIGN KEY (comment_id) REFERENCES Comment(id) ON DELETE CASCADE
);