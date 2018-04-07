import web
from queries import *

render_deep = web.template.render('templates/award/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Award:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(list(db.query(read_query({
							'selection': '*',
							'main_tbl': 'Award',
							'join_tbls': [],
							'criteria': [
								('Award', 'id', '=', id)
							]
						}))))

		if action_type == 'CRUD':
			return render_deep.crud_award()

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			award_name = data.award_name
			award_description = data.award_description
			db.query(insert_query({
				'table': 'Award',
				'k_list': ['id', 'award_name', 'award_description'],
				'v_list': [id, award_name, award_description]
			}))
			return web.seeother('/award/R?id={}'.format(id))

		if action_type == 'U':
			id = data.id
			award_name = data.award_name
			award_description = data.award_description
			db.query(update_query({
				'table': 'Award',
				'update_tuples': [
					('award_name', award_name),
					('award_description', award_description)
				],
				'criteria': [
					('Award', 'id', '=', id)
				]
			}))
			return web.seeother('/award/R?id={}'.format(id))

		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Award',
				'criteria': [
					('Award', 'id', '=', id)
				]
			}))
			return web.seeother('/award/CRUD')



