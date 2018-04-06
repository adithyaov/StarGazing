import web
from queries import *

render = web.template.render('templates/')

class Movie:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.index()

		if action_type == 'A':
			return render.test(best_movies())

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			movie_title = data.movie_title
			age_rating = data.age_rating
			release_date = data.release_date
			return insert_query({
				'table': 'Movie',
				'k_list': ['movie_title', 'age_rating', 'release_date'],
				'v_list': [movie_title, age_rating, release_date]
			})

		if action_type == 'U':
			id = data.id
			movie_title = data.movie_title
			age_rating = data.age_rating
			release_date = data.release_date
			return update_query({
				'table': 'Movie',
				'update_tuples': [
					('movie_title', movie_title),
					('age_rating', age_rating),
					('release_date', release_date)
				],
				'criteria': [
					('Movie', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Movie',
				'criteria': [
					('Movie', 'id', '==', id)
				]
			})



