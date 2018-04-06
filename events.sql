DELIMITER //
CREATE EVENT maintain_vote_consistancy
    on SCHEDULE EVERY 1 MINUTE DO
    BEGIN
        DELETE FROM Movie_user 
            WHERE movie_id in (SELECT change_id FROM Vote_consistancy WHERE from_table='Movie');
        DELETE FROM Vote_consistancy WHERE from_table='Movie';
        DELETE FROM Comment_user 
            WHERE comment_id in (SELECT change_id FROM Vote_consistancy WHERE from_table='Comment');
        DELETE FROM Vote_consistancy WHERE from_table='Comment';
    END//
DELIMITER ;


