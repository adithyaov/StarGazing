import web
from controllers.hello import Hello
from controllers.movie import Movie

urls = (
	'/test/(.+)', 'Movie',
    '/(.*)', 'Hello'
)

app = web.application(urls, globals())




if __name__ == "__main__":
    app.run()