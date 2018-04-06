import web
from queries import *

render = web.template.render('templates/')

class Role:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.test(read_query({
				'selection': '*',
				'main_tbl': 'Role',
				'join_tbls': [],
				'criteria': [
					('Role', 'id', '==', id)
				]
			}))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			role_title = data.role_title
			role_description = data.role_description
			return insert_query({
				'table': 'Role',
				'k_list': ['role_title', 'role_description'],
				'v_list': [role_title, role_description]
			})

		if action_type == 'U':
			id = data.id
			role_title = data.role_title
			role_description = data.role_description
			return update_query({
				'table': 'Role',
				'update_tuples': [
					('role_title', role_title),
					('role_description', role_description)
				],
				'criteria': [
					('Role', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Role',
				'criteria': [
					('Role', 'id', '==', id)
				]
			})



