import web
from queries import *

render = web.template.render('templates/')

class Stage:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.test(read_query({
				'selection': '*',
				'main_tbl': 'Stage',
				'join_tbls': [],
				'criteria': [
					('Stage', 'id', '==', id)
				]
			}))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			stage_name = data.stage_name
			stage_description = data.stage_description
			return insert_query({
				'table': 'Stage',
				'k_list': ['stage_name', 'stage_description'],
				'v_list': [stage_name, stage_description]
			})

		if action_type == 'U':
			id = data.id
			stage_name = data.stage_name
			stage_description = data.stage_description
			return update_query({
				'table': 'Stage',
				'update_tuples': [
					('stage_name', stage_name),
					('stage_description', stage_description)
				],
				'criteria': [
					('Stage', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Stage',
				'criteria': [
					('Stage', 'id', '==', id)
				]
			})



