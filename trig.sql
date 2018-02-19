DELIMITER //
CREATE TRIGGER t_update_movie_ratings_i 
 	AFTER INSERT ON Movie_user 
  	FOR EACH ROW 
  	BEGIN
		UPDATE Movie M
		SET M.avg_rating = f_calc_avg_rating(new.movie_id)
		WHERE M.id = new.movie_id;
   	END;
   //


  CREATE TRIGGER t_update_comment_ratings_i 
 	BEFORE INSERT ON Comment_user 
  	FOR EACH ROW 
  	IF New.vote  IN ('up') THEN
  	UPDATE Comment C 
  	SET C.upvotes = C.upvotes + 1
  	Where C.id = new.comment_id;
  	ELSE
  	UPDATE Comment C 
  	SET C.upvotes = C.upvotes + 1
  	Where C.id = new.comment_id;
  	END IF;
// 	

CREATE TRIGGER t_update_movie_ratings_u 
 	AFTER UPDATE ON Movie_user 
  	FOR EACH ROW 
  	BEGIN
		UPDATE Movie M
		SET M.avg_rating = f_calc_avg_rating(new.movie_id)
		WHERE M.id = new.movie_id;
   	END;
// 	