import web
from queries import *

render = web.template.render('templates/')

class Movie:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.test(one_movie({'id': id}))

		if action_type == 'A':
			return render.test(best_movies())

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			title = data.title
			age_r = data.age_r
			release = data.release
			return insert_query({
				'table': 'Movie',
				'k_list': ['title', 'age_rating', 'release_date'],
				'v_list': [title, age_r, release]
			})

		if action_type == 'U':
			id = data.id
			title = data.title
			age_r = data.age_r
			release = data.release
			return update_query({
				'table': 'Movie',
				'update_tuples': [
					('title', title),
					('age_rating', age_r),
					('release_date', release)
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



