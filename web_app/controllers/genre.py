import web
from queries import *

render = web.template.render('templates/')

class Genre:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.test(read_query({
				'selection': '*',
				'main_tbl': 'Genre',
				'join_tbls': [],
				'criteria': [
					('Genre', 'id', '==', id)
				]
			}))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			genre_name = data.genre_name
			genre_description = data.genre_description
			return insert_query({
				'table': 'Genre',
				'k_list': ['genre_name', 'genre_description'],
				'v_list': [genre_name, genre_description]
			})

		if action_type == 'U':
			id = data.id
			genre_name = data.genre_name
			genre_description = data.genre_description
			return update_query({
				'table': 'Genre',
				'update_tuples': [
					('genre_name', genre_name),
					('genre_description', genre_description)
				],
				'criteria': [
					('Genre', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Genre',
				'criteria': [
					('Genre', 'id', '==', id)
				]
			})



