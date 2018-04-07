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
			return render_shallow.crud_comment()

		if action_type == 'D':
			c_user_id = data.c_user_id
			movie_id = data.movie_id		
			id = data.id
			if str(c_user_id) != '1':

				if movie_id == None:
					return web.seeother('/comment/CRUD')
				return web.seeother('/movie/R?id={}'.format(movie_id))
			else:
				db.query(delete_query({
					'table': 'Comment',
					'criteria': [
						('Comment', 'id', '=', id)
					]
				}))

				if movie_id == None:
					return web.seeother('/comment/CRUD')
				return web.seeother('/movie/R?id={}'.format(movie_id))



	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.id
			content = data.content
			date_posted = '2018-4-7'
			movie_id = data.movie_id
			user_id = 1


			db.query(insert_query({
				'table': 'Comment',
				'k_list': ['id', 'content', 'date_posted', 'upvotes', 'downvotes', 'movie_id', 'user_id'],
				'v_list': [id, content, date_posted, 0, 0, movie_id, user_id]
			}))


			return web.seeother('/movie/R?id={}'.format(movie_id))

		if action_type == 'U':
			id = data.id
			movie_id = data.movie_id
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

			if movie_id == None:
				return web.seeother('/comment/CRUD')
			return web.seeother('/movie/R?id={}'.format(movie_id))



