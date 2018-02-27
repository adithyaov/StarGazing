-- Basic Idea
-- 2 type of roles
-- Basic, Main
-- Basic roles are independent
-- Main roles are dependent on Main (or/and) Basic roles
-- Basic roles, for each (Table, operation)

-- DROP TABLE IF EXISTS Award_mpr_stage;
-- DROP TABLE IF EXISTS Movie_person_role;

DROP TABLE IF EXISTS Award_mpr_stage;
DROP TABLE IF EXISTS Movie_person_role;
DROP TABLE IF EXISTS Genre_movie;
DROP TABLE IF EXISTS Movie_user;
DROP TABLE IF EXISTS Comment_user;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Comment;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Award;
DROP TABLE IF EXISTS Stage;

create role 'b_person_select';
create role 'b_person_update';
create role 'b_person_insert';
create role 'b_person_delete';
grant select on stargazing.Person to 'b_person_select';
grant update on stargazing.Person to 'b_person_update';
grant insert on stargazing.Person to 'b_person_insert';
grant delete on stargazing.Person to 'b_person_delete';

create role 'b_role_select';
create role 'b_role_update';
create role 'b_role_insert';
create role 'b_role_delete';
grant select on stargazing.Role to 'b_role_select';
grant update on stargazing.Role to 'b_role_update';
grant insert on stargazing.Role to 'b_role_insert';
grant delete on stargazing.Role to 'b_role_delete';

create role 'b_stage_select';
create role 'b_stage_update';
create role 'b_stage_insert';
create role 'b_stage_delete';
grant select on stargazing.Stage to 'b_stage_select';
grant update on stargazing.Stage to 'b_stage_update';
grant insert on stargazing.Stage to 'b_stage_insert';
grant delete on stargazing.Stage to 'b_stage_delete';

create role 'b_award_select';
create role 'b_award_update';
create role 'b_award_insert';
create role 'b_award_delete';
grant select on stargazing.Award to 'b_award_select';
grant update on stargazing.Award to 'b_award_update';
grant insert on stargazing.Award to 'b_award_insert';
grant delete on stargazing.Award to 'b_award_delete';

create role 'b_genre_select';
create role 'b_genre_update';
create role 'b_genre_insert';
create role 'b_genre_delete';
grant select on stargazing.Genre to 'b_genre_select';
grant update on stargazing.Genre to 'b_genre_update';
grant insert on stargazing.Genre to 'b_genre_insert';
grant delete on stargazing.Genre to 'b_genre_delete';

create role 'b_movie_select';
create role 'b_movie_update';
create role 'b_movie_insert';
create role 'b_movie_delete';
grant select on stargazing.Movie to 'b_movie_select';
grant update on stargazing.Movie to 'b_movie_update';
grant insert on stargazing.Movie to 'b_movie_insert';
grant delete on stargazing.Movie to 'b_movie_delete';

create role 'b_user_select';
create role 'b_user_update';
create role 'b_user_insert';
create role 'b_user_delete';
grant select on stargazing.User to 'b_user_select';
grant update on stargazing.User to 'b_user_update';
grant insert on stargazing.User to 'b_user_insert';
grant delete on stargazing.User to 'b_user_delete';

create role 'b_comment_select';
create role 'b_comment_update';
create role 'b_comment_insert';
create role 'b_comment_delete';
grant select on stargazing.Comment to 'b_comment_select';
grant update on stargazing.Comment to 'b_comment_update';
grant insert on stargazing.Comment to 'b_comment_insert';
grant delete on stargazing.Comment to 'b_comment_delete';

create role 'b_comment_user_select';
create role 'b_comment_user_update';
create role 'b_comment_user_insert';
create role 'b_comment_user_delete';
grant select on stargazing.Comment_user to 'b_comment_user_select';
grant update on stargazing.Comment_user to 'b_comment_user_update';
grant insert on stargazing.Comment_user to 'b_comment_user_insert';
grant delete on stargazing.Comment_user to 'b_comment_user_delete';

create role 'b_movie_user_select';
create role 'b_movie_user_update';
create role 'b_movie_user_insert';
create role 'b_movie_user_delete';
grant select on stargazing.Movie_user to 'b_movie_user_select';
grant update on stargazing.Movie_user to 'b_movie_user_update';
grant insert on stargazing.Movie_user to 'b_movie_user_insert';
grant delete on stargazing.Movie_user to 'b_movie_user_delete';

create role 'b_genre_movie_select';
create role 'b_genre_movie_update';
create role 'b_genre_movie_insert';
create role 'b_genre_movie_delete';
grant select on stargazing.Genre_movie to 'b_genre_movie_select';
grant update on stargazing.Genre_movie to 'b_genre_movie_update';
grant insert on stargazing.Genre_movie to 'b_genre_movie_insert';
grant delete on stargazing.Genre_movie to 'b_genre_movie_delete';

create role 'b_movie_person_role_select';
create role 'b_movie_person_role_update';
create role 'b_movie_person_role_insert';
create role 'b_movie_person_role_delete';
grant select on stargazing.Movie_person_role to 'b_movie_person_role_select';
grant update on stargazing.Movie_person_role to 'b_movie_person_role_update';
grant insert on stargazing.Movie_person_role to 'b_movie_person_role_insert';
grant delete on stargazing.Movie_person_role to 'b_movie_person_role_delete';

create role 'b_award_mpr_stage_select';
create role 'b_award_mpr_stage_update';
create role 'b_award_mpr_stage_insert';
create role 'b_award_mpr_stage_delete';
grant select on stargazing.Award_mpr_stage to 'b_award_mpr_stage_select';
grant update on stargazing.Award_mpr_stage to 'b_award_mpr_stage_update';
grant insert on stargazing.Award_mpr_stage to 'b_award_mpr_stage_insert';
grant delete on stargazing.Award_mpr_stage to 'b_award_mpr_stage_delete';

