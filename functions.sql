CREATE FUNCTION f_calc_avg_rating(INT m_id)
RETURNS INT return (SELECT AVG(rating) FROM Movie_user WHERE movie_id = m_id);