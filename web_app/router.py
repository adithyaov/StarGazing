import web
from controllers.hello import Hello
from controllers.movie import Movie
from controllers.award import Award
from controllers.movie_user import Movie_user
from controllers.comment_user import Comment_user

urls = (
	'/award/(.+)', 'Award',
	'/movie/(.+)', 'Movie',
	'/movie_user/(.+)', 'Movie_user',
	'/comment_user/(.+)', 'Comment_user',
    '/(.*)', 'Hello'
)

app = web.application(urls, globals())




if __name__ == "__main__":
    app.run()