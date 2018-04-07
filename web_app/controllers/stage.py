import web
from queries import *

render_deep = web.template.render('templates/stage/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Stage:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(read_query({
				'selection': '*',
				'main_tbl': 'Stage',
				'join_tbls': [],
				'criteria': [
					('Stage', 'id', '=', id)
				]
			}))

		if action_type == 'CRUD':
			return render_deep.crud_stage()


	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			stage_name = data.stage_name
			stage_description = data.stage_description
			db.query(insert_query({
				'table': 'Stage',
				'k_list': ['id', 'stage_name', 'stage_description'],
				'v_list': [id, stage_name, stage_description]
			}))
			return web.seeother('/stage/R?id={}'.format(id))


		if action_type == 'U':
			id = data.id
			stage_name = data.stage_name
			stage_description = data.stage_description
			db.query(update_query({
				'table': 'Stage',
				'update_tuples': [
					('stage_name', stage_name),
					('stage_description', stage_description)
				],
				'criteria': [
					('Stage', 'id', '=', id)
				]
			}))
			return web.seeother('/role/R?id={}'.format(id))


		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Stage',
				'criteria': [
					('Stage', 'id', '==', id)
				]
			}))
			return web.seeother('/stage/CRUD')



