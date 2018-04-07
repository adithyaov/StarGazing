import web
from queries import *

render_deep = web.template.render('templates/comment/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Comment:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			return render_shallow.general_display(list(db.query(read_query({
							'selection': '*',
							'main_tbl': 'Comment',
							'join_tbls': [],
							'criteria': [
								('Comment', 'id', '=', id)
							]
						}))))

		if action_type == 'CRUD':
			return render_deep.crud_comment()

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			content = data.content
			date_posted = data.date_posted
			upvotes = data.upvotes
			downvotes = data.downvotes
			movie_id = data.movie_id
			user_id = data.user_id


			db.query(insert_query({
				'table': 'Comment',
				'k_list': ['id', 'content', 'date_posted','upvotes','downvotes','movie_id','user_id'],
				'v_list': [id, content, date_posted,upvotes,downvotes,movie_id,user_id]
			}))
			return web.seeother('/comment/R?id={}'.format(id))

		if action_type == 'U':
			id = data.id
			content = data.content
			db.query(update_query({
				'table': 'Comment',
				'update_tuples': [
					('content', content)
	
				],
				'criteria': [
					('Comment', 'id', '=', id)
				]
			}))
			return web.seeother('/comment/R?id={}'.format(id))

		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Comment',
				'criteria': [
					('Comment', 'id', '=', id)
				]
			}))
			return web.seeother('/comment/CRUD')



