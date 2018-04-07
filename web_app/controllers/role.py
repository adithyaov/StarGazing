import web
from queries import *

render_deep = web.template.render('templates/role/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Role:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(read_query({
				'selection': '*',
				'main_tbl': 'Role',
				'join_tbls': [],
				'criteria': [
					('Role', 'id', '=', id)
				]
			}))

		if action_type == 'CRUD':
			return render_deep.crud_role()


	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			role_title = data.role_title
			role_description = data.role_description
			db.query(insert_query({
				'table': 'Role',
				'k_list': ['id', 'role_title', 'role_description'],
				'v_list': [id, role_title, role_description]
			}))
			return web.seeother('/role/R?id={}'.format(id))


		if action_type == 'U':
			id = data.id
			role_title = data.role_title
			role_description = data.role_description
			db.query(update_query({
				'table': 'Role',
				'update_tuples': [
					('role_title', role_title),
					('role_description', role_description)
				],
				'criteria': [
					('Role', 'id', '=', id)
				]
			}))
			return web.seeother('/role/R?id={}'.format(id))


		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Role',
				'criteria': [
					('Role', 'id', '=', id)
				]
			}))
			return web.seeother('/role/CRUD')



