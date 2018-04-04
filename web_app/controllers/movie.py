from queries import *
import json

class Movie:
	def GET(self, action_type, action_params):
		action_params = json.loads(action_params)
		return one_movie(action_params)



