class Hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'