DROP TABLE IF EXISTS Award_mpr_stage;
DROP TABLE IF EXISTS Movie_person_role;
DROP TABLE IF EXISTS Genre_movie;

INSERT INTO Award (id, award_name, award_description) VALUES
	(1, 'Best Actor', 'Award for being the best!'),
	(2, 'Best Actress', 'Award for being the best!'),
	(3, 'Best Debut Actor', 'Award for being the best!'),
	(4, 'Best Anatagonist', 'Award for being the best!'),
	(5, 'Best Supporting Role (Male)', 'Award for being the best!'),
	(6, 'Best Supporting Role (Female)', 'Award for being the best!'),
	(7, 'Best Director', 'Award for being the best!');

INSERT INTO Movie (id, movie_title, release_date, age_rating) VALUES
	(1, 'The Matrix', '1999-12-04', 18),
	(2, 'The Matrix II', '2333-12-04', 21),
	(3, 'The God Father', '3222-12-04', 25),
	(4, 'Awe', '3333-12-04', 18),
	(5, 'Inception', '1112-12-04', 16),
	(6, 'Toy Story', '2222-12-04', 12);

INSERT INTO Genre (id, genre_name, genre_description) VALUES
	(1, 'Sci-fi', 'Unreal!'),
	(2, 'Action', 'Go Jackie!'),
	(3, 'Drama', 'Chobey'),
	(4, 'Kids', 'Innocent angels'),
	(5, 'Spice of Life', '3-gatsu no is the best');

INSERT INTO Stage (id, stage_name, stage_description) VALUES
	(1, 'Oscar', 'Cool!'),
	(2, 'IIFA', 'Lame!'),
	(3, 'FIFA', 'What is this doing here?'),
	(4, 'LIFA', 'huh? Im an idiot'),
	(5, 'Worst awards ever', 'I like this!');

INSERT INTO Role (id, role_title, role_description) VALUES
	(1, 'Actor', 'The hero!'),
	(2, 'Actress', 'The hot girl'),
	(3, 'Maid', 'The other hot girl?'),
	(4, 'Side Character 1', 'GAY!'),
	(5, 'Black Dude', 'dies first'),
	(6, 'Antagonist', 'Awesome guy');

INSERT INTO Person (id, first_name, last_name, dob, bio) VALUES
	(1, 'Keanue', 'Reeves', '1965-03-04', 'No bio yet :-('),
	(2, 'Tom', 'Cruise', '1962-10-10', 'No bio yet :-('),
	(3, 'Gaikwad', 'Shivaji', '1935-03-05', 'No bio yet :-('),
	(4, 'Leo', 'Decaprio', '1235-01-06', 'No bio yet :-('),
	(5, 'Robert de', 'Nero', '1455-06-04', 'No bio yet :-('),
	(6, 'Buzz', 'Lighter', '1966-05-08', 'No bio yet :-(');

INSERT INTO User (id, name, email, password_hash, dob) VALUES
	(1, 'kothari', 'k@noob.com', '0000', '1996-02-02'),
	(2, 'mayank', 'only@ww.com', 'ilovemetha', '1996-08-08'),
	(3, 'bono', 'true_noob@useless.com', 'noobparanioa', '1999-09-09'),
	(4, 'chobs', 'paper_guy@ieee.com', 'peacemaker', '1996-01-01');

INSERT INTO Comment (id, content, date_posted, movie_id, user_id) VALUES
	(1, 
		'This movie is awesome!', 
		'2018-01-01',
		1, 1),
	(2, 
		'A good psycological movie!', 
		'2018-01-01',
		4, 2),
	(3, 
		'Dreams are so complex!', 
		'2018-01-01',
		5, 2),
	(4, 
		'Old but gold!', 
		'2018-01-01',
		3, 3),
	(5, 
		'When is Matrix 3 coming out?!', 
		'2018-01-01',
		2, 4),
	(6, 
		'This touched my heart!', 
		'2018-01-01',
		6, 4);

INSERT INTO Comment_user (comment_id, user_id, vote) VALUES
    (1, 1, 'up'),
    (2, 2, 'up'),
    (3, 3, 'up'),
    (4, 4, 'up'),
    (5, 1, 'up'),
    (6, 2, 'up'),
    (1, 3, 'up'),
    (2, 4, 'up'),
    (3, 1, 'up'),
    (4, 2, 'down'),
    (5, 3, 'down'),
    (6, 4, 'down'),
    (1, 2, 'down'),
    (2, 3, 'down'),
    (3, 4, 'down');

INSERT INTO Comment_user (movie_id, user_id, rating) VALUES
    (1, 1, 3),
    (2, 2, 4),
    (3, 3, 5),
    (4, 4, 2),
    (5, 1, 3),
    (6, 2, 5),
    (1, 3, 0),
    (2, 4, 3),
    (3, 1, 2),
    (4, 2, 5),
    (5, 3, 5),
    (6, 4, 4),
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 2);

