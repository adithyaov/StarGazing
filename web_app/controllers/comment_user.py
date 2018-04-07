import web
from queries import *

render = web.template.render('templates/')

class Comment_user:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			comment_id = data.comment_id
			user_id = data.user_id
			return render_shallow.general_display(list(db.query(read_query({
							'selection': '*',
							'main_tbl': 'Comment_user',
							'join_tbls': [],
							'criteria': [
								('Comment_user', 'comment_id', '=', comment_id),
								('Comment_user', 'user_id', '=', user_id)
							]
						}))))

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			comment_id = data.comment_id
			user_id = data.user_id
			rating = data.rating
			return insert_query({
				'table': 'Comment_user',
				'k_list': ['comment_id', 'user_id', 'rating'],
				'v_list': [comment_id, user_id, rating]
			})

		if action_type == 'D':			
			comment_id = data.comment_id
			user_id =  data.user_id
			return delete_query({
				'table': 'Comment_user',
				'criteria': [
					('Comment_user', 'comment_id', '==', comment_id)
					('Comment_user', 'user_id', '==', user_id)
				]
			})



