import web
from queries import *

render_deep = web.template.render('templates/movie/')
render_shallow = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='kidvscat', db='stargazing')

class Movie:
	def GET(self, action_type):
		data = web.input()
		if action_type == 'R':
			id = data.id
			(status, queries) = one_movie({'id':id})
			results = [list(db.query(x)) for x in queries]
			return render_deep.main(results[0], results[1], results[2])

		if action_type == 'A':
			(status, q) = best_movies()
			return render_shallow.test(list(db.query(q)))
			
		if action_type == 'U':
			(status, q) = upcoming_movies()
			return render_shallow.test(list(db.query(q)))

		if action_type == 'EH':
			id = data.id
			
			return render_shallow.general_display(list(db.query(read_query({
					'selection': '*',
					'main_tbl': 'Movie_edit_history',
					'join_tbls': [],
					'criteria': [
						('Movie_edit_history', 'movie_id', '=', id)
					]
				}))))

		if action_type == 'CRUD':
			return render_deep.crud_movie()


	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			id = data.movie_id
			movie_title = data.movie_title
			age_rating = data.age_rating
			release_date = data.release_date
			db.query(insert_query({
				'table': 'Movie',
				'k_list': ['id', 'movie_title', 'age_rating', 'release_date'],
				'v_list': [id, movie_title, age_rating, release_date]
			}))
			return web.seeother('/movie/R?id={}'.format(id))


		if action_type == 'U':
			id = data.id
			movie_title = data.movie_title
			age_rating = data.age_rating
			release_date = data.release_date
			db.query(update_query({
				'table': 'Movie',
				'update_tuples': [
					('movie_title', movie_title),
					('age_rating', age_rating),
					('release_date', release_date)
				],
				'criteria': [
					('Movie', 'id', '=', id)
				]
			}))
			return web.seeother('/movie/R?id={}'.format(id))


		if action_type == 'D':			
			id = data.id
			db.query(delete_query({
				'table': 'Movie',
				'criteria': [
					('Movie', 'id', '=', id)
				]
			}))
			return web.seeother('/movie/CRUD')




