

-- Gets all movie which has rating above a rating level (works)
DROP PROCEDURE movie_rating_gt;     
DELIMITER //
CREATE PROCEDURE movie_rating_gt(IN rating_level INT)
BEGIN   
    SELECT * FROM Movie WHERE Movie.avg_rating > rating_level;
END//
DELIMITER ;
-- Gets avg rating of movie with movie id 
DROP PROCEDURE avg_ratings_of_movie;
DELIMITER //
CREATE PROCEDURE avg_ratings_of_movie(IN m_id INT)
BEGIN
    SELECT avg(rating) FROM Movie_user WHERE movie_id = m_id;
END//
DELIMITER ;

DROP PROCEDURE avg_ratings_of_person;
DELIMITER //
CREATE PROCEDURE avg_ratings_of_person(IN person_id INT)
BEGIN
    SELECT AVG(avg_rating) FROM Movie WHERE Movie.id IN
        (SELECT movie_id FROM Movie_person_role WHERE person_id = person_id);
END//
DELIMITER ;

DROP PROCEDURE num_movies_of_person;
DELIMITER //
CREATE PROCEDURE num_movies_of_person(IN person_id INT)
BEGIN
    SELECT COUNT(*) FROM Movie WHERE Movie.id IN
        (SELECT movie_id FROM Movie_person_role WHERE person_id = person_id);
END//
DELIMITER ;


DROP PROCEDURE get_awards_person;
DELIMITER //
CREATE PROCEDURE get_awards_person(IN person_id INT)
BEGIN
    SELECT Award.award_name, Stage.stage_name
        FROM Award_mpr_stage as ams
        JOIN Movie_person_role as mpr on ams.mpr_id = mpr.id
        JOIN Award on Award.id = ams.award_id
        JOIN Stage on Stage.id = ams.stage_id
        WHERE mpr.person_id = person_id;
END//
DELIMITER ;


DROP PROCEDURE top_10_of;
DELIMITER //
CREATE PROCEDURE top_10_of(IN in_year INT, IN genre_id INT)
BEGIN
    SELECT m.id, m.movie_title, m.release_date, m.age_rating, m.avg_rating
        FROM Genre_movie as gm
        JOIN Movie as m on gm.movie_id = m.id
        JOIN Genre as g on gm.genre_id = m.id
        WHERE YEAR(m.release_date) = in_year
            AND g.id = genre_id
        ORDER BY m.avg_rating DESC
        LIMIT 10;
END//
DELIMITER ;

DROP PROCEDURE roles_by_person;
DELIMITER //
CREATE PROCEDURE roles_by_person(IN person_id INT)
BEGIN
    SELECT m.movie_title, r.role_title FROM Movie_person_role as mpr
        JOIN Movie as m on mpr.movie_id = m.id
        JOIN Role as r on mpr.role_id = r.id
        WHERE mpr.person_id = person_id;
END//
DELIMITER ;

DROP PROCEDURE comment_voters;
DELIMITER //
CREATE PROCEDURE comment_voters(IN comment_id INT, IN vote_status VARCHAR(2))
BEGIN
    SELECT u.id, u.name, u.email FROM Comment_user as cu
        JOIN Comment as c on cu.comment_id = c.id
        JOIN User as u on cu.user_id = u.id
        WHERE cu.vote = vote_status;
END//
DELIMITER ;

DROP PROCEDURE movie_raters;
DELIMITER //
CREATE PROCEDURE movie_raters(IN movie_id INT)
BEGIN
    SELECT u.id, u.name, u.email, mu.rating FROM Movie_user as mu
        JOIN User as u on mu.user_id = u.id
        WHERE mu.movie_id = movie_id;
END//
DELIMITER ;

DROP PROCEDURE award_in_year;
DELIMITER //
CREATE PROCEDURE award_in_year(IN award_id INT, IN year INT)
BEGIN
    SELECT p.id, p.first_name, p.last_name, p.dob FROM Award_mpr_stage as ams
        JOIN Movie_person_role as mpr on ams.mpr_id = mpr.id
        JOIN Person as p on mpr.person_id = p.id
        WHERE ams.award_id = award_id
            AND YEAR(ams.won_in) = year;
END//
DELIMITER ;


DROP PROCEDURE  get_cast_of_movie;
DELIMITER //
CREATE PROCEDURE get_cast_of_movie (IN movie_id INT)
BEGIN
    SELECT m.movie_title, p.first_name, p.last_name,r.role_title FROM Movie as m, Person as p, Role as r, Movie_person_role as mpr
    WHERE mpr.movie_id = movie_id and mpr.role_id =  r.id and mpr.person_id = p.id and mpr.movie_id=m.id;
END//
DELIMITER ;
