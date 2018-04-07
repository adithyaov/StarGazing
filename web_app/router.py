import web
from controllers.hello import Hello
from controllers.movie import Movie
from controllers.award import Award

urls = (
	'/award/(.+)', 'Award',
	'/test/(.+)', 'Movie',
    '/(.*)', 'Hello'
)

app = web.application(urls, globals())




if __name__ == "__main__":
    app.run()