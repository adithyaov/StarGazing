import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

db = web.database(dbn='mysql', db='stargazing', user='root', pw='')


class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()