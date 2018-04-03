-- trigger is called when new rating is given by an user to a movie (checked)
DROP TRIGGER t_update_movie_ratings_i; 
DELIMITER //
CREATE TRIGGER t_update_movie_ratings_i
AFTER INSERT ON Movie_user 
FOR EACH ROW 
BEGIN 
    UPDATE Movie M
    SET M.avg_rating = f_avg_ratings_of_movie(new.movie_id)
    WHERE M.id = new.movie_id;
END//
DELIMITER ;
-- trigger is called when new rating is given by an user to a comment
DROP TRIGGER t_update_comment_ratings_i; 
DELIMITER //
CREATE TRIGGER t_update_comment_ratings_i 
BEFORE INSERT ON Comment_user
FOR EACH ROW 
BEGIN
    IF New.vote  IN ('up') THEN
        UPDATE Comment C 
        SET C.upvotes = C.upvotes + 1
        WHERE C.id = new.comment_id;
    ELSE
        UPDATE Comment C 
        SET C.downvotes = C.downvotes + 1
        WHERE C.id = new.comment_id;
    END IF;
END//
DELIMITER ;
-- trigger is called when  rating  given by an user  to a movie is changed.    (checked)
DROP TRIGGER t_update_movie_ratings_u;
DELIMITER //
CREATE TRIGGER t_update_movie_ratings_u 
AFTER UPDATE ON Movie_user 
FOR EACH ROW 
BEGIN
    UPDATE Movie M
    SET M.avg_rating = f_avg_ratings_of_movie(new.movie_id)
    WHERE M.id = new.movie_id;
END//
DELIMITER ;
-- trigger is called when  rating  given by an user  to a comment is changed. (checked)    
DROP TRIGGER t_update_comment_ratings_u;
DELIMITER //
CREATE TRIGGER t_update_comment_ratings_u
BEFORE UPDATE ON Comment_user 
FOR EACH ROW 
BEGIN
    IF New.vote  IN ('up')  AND Old.vote IN ('down') THEN
        UPDATE Comment C 
        SET C.upvotes = C.upvotes + 1 ,C.downvotes = C.downvotes - 1
        WHERE C.id = new.comment_id;
    END IF;
    IF New.vote  IN ('down')  AND Old.vote IN ('up') THEN
        UPDATE Comment C 
        SET C.upvotes = C.upvotes - 1 ,C.downvotes = C.downvotes + 1
        WHERE C.id = new.comment_id;
    END IF;
END//
DELIMITER ;
-- trigger is called when  rating  given by an user to a movie is deleted.   (checked)
DROP TRIGGER t_update_movie_ratings_d;
DELIMITER //
CREATE TRIGGER t_update_movie_ratings_d
AFTER DELETE ON Movie_user 
FOR EACH ROW 
BEGIN
    UPDATE Movie M
    SET M.avg_rating = f_avg_ratings_of_movie(old.movie_id)
    WHERE M.id = old.movie_id;
END//
DELIMITER ;
-- trigger is called when  rating  given by an user to a comment is deleted.
DROP TRIGGER t_update_comment_ratings_d;
DELIMITER //
CREATE TRIGGER t_update_comment_ratings_d
BEFORE DELETE ON Comment_user 
FOR EACH ROW
BEGIN
    IF old.vote  IN ('up') THEN
        UPDATE Comment C 
        SET C.upvotes = C.upvotes  - 1
        WHERE C.id = old.comment_id;
    ELSE
        UPDATE Comment C 
        SET C.downvotes = C.downvotes - 1
        WHERE C.id = old.comment_id;
    END IF;
END//
DELIMITER ;
-- this trigger keeps edit history of comments
DROP TRIGGER t_change_comment_content;
DELIMITER //
CREATE TRIGGER t_change_comment_content
AFTER UPDATE ON Comment 
FOR EACH ROW 
BEGIN
    IF NEW.content <> OLD.content THEN
        INSERT INTO Comment_edit_history values (NEW.id, NEW.content,CURTIME());
    END IF;
END//
DELIMITER ;
-- this trigger keeps edit history of movies title    (checked)
DROP TRIGGER t_change_movie_content;  
DELIMITER //
CREATE TRIGGER t_change_movie_content
AFTER UPDATE ON Movie 
FOR EACH ROW 
BEGIN
    IF NEW.movie_title <> OLD.movie_title THEN
       INSERT INTO Movie_edit_history values (NEW.id,NEW.movie_title,CURTIME());
    END IF;
END//
DELIMITER ;
