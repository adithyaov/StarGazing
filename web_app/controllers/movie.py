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

	def POST(self, action_type):

		data = web.input()

		if action_type == 'C':
			movie_title = data.movie_title
			age_rating = data.age_rating
			release_date = data.release_date
			return insert_query({
				'table': 'Movie',
				'k_list': ['movie_title', 'age_rating', 'release_date'],
				'v_list': [movie_title, age_rating, release_date]
			})

		if action_type == 'U':
			id = data.id
			movie_title = data.movie_title
			age_rating = data.age_rating
			release_date = data.release_date
			return update_query({
				'table': 'Movie',
				'update_tuples': [
					('movie_title', movie_title),
					('age_rating', age_rating),
					('release_date', release_date)
				],
				'criteria': [
					('Movie', 'id', '==', id)
				]
			})

		if action_type == 'D':			
			id = data.id
			return delete_query({
				'table': 'Movie',
				'criteria': [
					('Movie', 'id', '==', id)
				]
			})



