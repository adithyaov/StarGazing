import web
from queries import *

render = web.template.render('templates/')

class Movie_user:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			movie_id = data.movie_id
			user_id = data.user_id
			return render_shallow.general_display(list(db.query(read_query({
							'selection': '*',
							'main_tbl': 'Movie_user',
							'join_tbls': [],
							'criteria': [
								('Movie_user', 'movie_id', '=', movie_id),
								('Movie_user', 'user_id', '=', user_id)
							]
						}))))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			movie_id = data.movie_id
			user_id = data.user_id
			rating = data.rating
			return insert_query({
				'table': 'Movie_user',
				'k_list': ['movie_id', 'user_id', 'rating'],
				'v_list': [movie_id, user_id, rating]
			})

		if action_type == 'D':			
			movie_id = data.movie_id
			user_id =  data.user_id
			return delete_query({
				'table': 'Movie_user',
				'criteria': [
					('Movie_user', 'movie_id', '==', movie_id)
					('Movie_user', 'user_id', '==', user_id)
				]
			})



