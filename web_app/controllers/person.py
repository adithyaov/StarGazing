import web
from queries import *

render_deep = web.template.render('templates/person/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')


class Person:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(list(db.query(read_query({
							'selection': '*',
							'main_tbl': 'Person',
							'join_tbls': [],
							'criteria': [
								('Person', 'id', '=', id)
							]
						}))))

		if action_type == 'CRUD':
			return render_shallow.crud_person()

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			first_name = data.first_name
			last_name = data.last_name
			dob = data.dob
			bio = data.bio
			db.query(insert_query({
				'table': 'Person',
				'k_list': ['id', 'first_name', 'last_name', 'dob', 'bio'],
				'v_list': [id, first_name, last_name, dob, bio]
			}))
			return web.seeother('/person/R?id={}'.format(id))

		if action_type == 'U':
			id = data.id
			first_name = data.first_name
			last_name = data.last_name
			dob = data.dob
			bio = data.bio
			db.query(update_query({
				'table': 'Person',
				'update_tuples': [
					('first_name', first_name),
					('last_name', last_name),
					('dob', dob),
					('bio', bio)
				],
				'criteria': [
					('Person', 'id', '=', id)
				]
			}))
			return web.seeother('/person/R?id={}'.format(id))


		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Person',
				'criteria': [
					('Person', 'id', '=', id)
				]
			}))
			return web.seeother('/person/CRUD')




