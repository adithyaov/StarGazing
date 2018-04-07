import web
from queries import *

render_deep = web.template.render('templates/genre/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Genre:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(list(db.query(read_query({
				'selection': '*',
				'main_tbl': 'Genre',
				'join_tbls': [],
				'criteria': [
					('Genre', 'id', '=', id)
				]
			}))))

		if action_type == 'CRUD':
			return render_deep.crud_genre()

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			genre_name = data.genre_name
			genre_description = data.genre_description
			db.query(insert_query({
				'table': 'Genre',
				'k_list': ['id', 'genre_name', 'genre_description'],
				'v_list': [id, genre_name, genre_description]
			}))
			return web.seeother('/genre/R?id={}'.format(id))


		if action_type == 'U':
			id = data.id
			genre_name = data.genre_name
			genre_description = data.genre_description
			db.query(update_query({
				'table': 'Genre',
				'update_tuples': [
					('genre_name', genre_name),
					('genre_description', genre_description)
				],
				'criteria': [
					('Genre', 'id', '=', id)
				]
			}))
			return web.seeother('/genre/R?id={}'.format(id))


		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Genre',
				'criteria': [
					('Genre', 'id', '=', id)
				]
			}))
			return web.seeother('/genre/CRUD')




