import web
from queries import *

render_deep = web.template.render('templates/comment_user/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

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

		if action_type == 'C':
			movie_id = data.movie_id			
			comment_id = data.comment_id
			user_id = data.user_id
			vote = data.vote
			db.query(insert_query({
				'table': 'Comment_user',
				'k_list': ['comment_id', 'user_id', 'vote'],
				'v_list': [comment_id, user_id, vote]
			}))
			return web.seeother('/movie/R?id={}'.format(movie_id))


		if action_type == 'D':
			movie_id = data.movie_id			
			comment_id = data.comment_id
			user_id =  data.user_id
			db.query(delete_query({
				'table': 'Comment_user',
				'criteria': [
					('Comment_user', 'comment_id', '=', comment_id),
					('Comment_user', 'user_id', '=', user_id)
				]
			}))
			return web.seeother('/movie/R?id={}'.format(movie_id))



