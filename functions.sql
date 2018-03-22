-- no functions

DROP FUNCTION f_avg_ratings_of_movie;
CREATE FUNCTION f_avg_ratings_of_movie(m_id INT)
    RETURNS FLOAT
    RETURN (SELECT avg(rating) FROM Movie_user WHERE movie_id = m_id);