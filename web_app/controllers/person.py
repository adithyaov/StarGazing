import web
from queries import *

render = web.template.render('templates/')

class Person:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.test(one_person({'id': id}))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			first_name = data.first_name
			last_name = data.last_name
			dob = data.dob
			bio = data.bio
			return insert_query({
				'table': 'Person',
				'k_list': ['first_name', 'last_name', 'dob', 'bio'],
				'v_list': [first_name, last_name, dob, bio]
			})

		if action_type == 'U':
			id = data.id
			first_name = data.first_name
			last_name = data.last_name
			dob = data.dob
			bio = data.bio
			return update_query({
				'table': 'Person',
				'update_tuples': [
					('first_name', first_name),
					('last_name', last_name),
					('dob', dob),
					('bio', bio)
				],
				'criteria': [
					('Person', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Person',
				'criteria': [
					('Person', 'id', '==', id)
				]
			})



