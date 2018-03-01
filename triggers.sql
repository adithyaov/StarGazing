DELIMITER //
CREATE TRIGGER t_update_movie_ratings_i
AFTER INSERT ON Movie_user 
FOR EACH ROW 
BEGIN 
    UPDATE Movie M
    SET M.avg_rating = f_calc_avg_rating(new.movie_id)
    WHERE M.id = new.movie_id;
END//
DELIMITER ;

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

DELIMITER //
CREATE TRIGGER t_update_movie_ratings_u 
AFTER UPDATE ON Movie_user 
FOR EACH ROW 
BEGIN
    UPDATE Movie M
    SET M.avg_rating = f_calc_avg_rating(new.movie_id)
    WHERE M.id = new.movie_id;
END//
DELIMITER ;

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

DELIMITER //
CREATE TRIGGER t_update_movie_ratings_d
AFTER DELETE ON Movie_user 
FOR EACH ROW 
BEGIN
    UPDATE Movie M
    SET M.avg_rating = f_calc_avg_rating(old.movie_id)
    WHERE M.id = old.movie_id;
END//
DELIMITER ;

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

DELIMITER //
CREATE TRIGGER t_change_comment_content
AFTER UPDATE ON Comment 
FOR EACH ROW 
BEGIN
    IF NEW.content <> OLD.content THEN
        UPDATE Comment C
        SET C.upvotes = 0, C.downvotes = 0,
            C.dateposted = CURRENT_DATE
        WHERE C.id = new.id;
    END IF;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER t_change_movie_content
AFTER UPDATE ON Movie 
FOR EACH ROW 
BEGIN
    IF NEW.movie_title <> OLD.movie_title THEN
        UPDATE Movie M
        SET M.avg_rating = 0
        WHERE M.id = new.id;
    END IF;
END//
DELIMITER ;
