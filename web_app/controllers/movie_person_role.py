import web
from queries import *

render_deep = web.template.render('templates/movie_person_role/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Movie_person_role:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(list(db.query(read_query({
							'selection': '*',
							'main_tbl': 'Movie_person_role',
							'join_tbls': [],
							'criteria': [
								('Movie_person_role', 'id', '=', id)
							]
						}))))

		if action_type == 'CRUD':
			return render_deep.crud_comment()

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			role_id = data.role_id
			movie_id = data.movie_id
			user_id = data.user_id


			db.query(insert_query({
				'table': 'Movie_person_role',
				'k_list': ['id', 'role_id','movie_id','user_id'],
				'v_list': [id, role_id,movie_id,user_id]
			}))
			return web.seeother('/movie_person_role/R?id={}'.format(id))


		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Movie_person_role',
				'criteria': [
					('Movie_person_role', 'id', '=', id)
				]
			}))
		



