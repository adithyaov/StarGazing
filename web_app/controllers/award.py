import web
from queries import *

render = web.template.render('templates/')

class Award:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render.test(read_query({
				'selection': '*',
				'main_tbl': 'Award',
				'join_tbls': [],
				'criteria': [
					('Award', 'id', '==', id)
				]
			}))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			award_name = data.award_name
			award_desc = data.award_desc
			return insert_query({
				'table': 'Award',
				'k_list': ['award_name', 'award_description'],
				'v_list': [award_name, award_desc]
			})

		if action_type == 'U':
			id = data.id
			award_name = data.award_name
			award_desc = data.award_desc
			return update_query({
				'table': 'Award',
				'update_tuples': [
					('award_name', award_name),
					('award_description', award_desc)
				],
				'criteria': [
					('Award', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Award',
				'criteria': [
					('Award', 'id', '==', id)
				]
			})



