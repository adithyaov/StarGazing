'''
Functions:

movie
movies

Person

advance search for movies

user system
can comment
can upvote/downvote
can rate

admin system
	for all type of admins

'''

'''
helpers
'''

def deny_response(arg):
	return False

def build_query(arg):
	selection = arg['selection']
	main_tbl = arg['main_tbl']
	join_tbls = arg['join_tbls']
	criteria = arg['criteria']
	'''
	join_tbls
	[
		(join_type, (table1, col_name), (table2, col_name))
	]
	criteria
	[
		(table, column, equality, value)
	]
	'''
	query_list = []

	'''
	init query
	'''
	query_list.append(
		'select {selection} from {main_tbl} as {main_tbl}'
		.format(main_tbl=main_tbl, selection=selection)
	)

	'''
	include joins
	'''
	for (join_type, (table1, col1), (table2, col2)) in join_tbls:
		query_list.append(
			'{join_type} join {table1} as {table1} on {table1}.{col1}={table2}.{col2}'
			.format(join_type=join_type, table1=table1, table2=table2, col1=col1, col2=col2)
		)

	'''
	where
	'''
	if len(criteria) > 0:
		query_list.append('where')
	for (table, column, equality, value) in criteria:
		query_list.append('{}.{} {} {}'.format(table, column, equality, value))
		query_list.append('and')

	return ' '.join(query_list[:-1])


print build_query({
	'selection': '*',
	'main_tbl': 'Movie',
	'join_tbls': [
		('inner', ('Person', 'id'), ('Truck', 'person_id'))
	],
	'criteria': [
		('Person', 'id', '>=', '200'),
		('Person', 'name', '==', '\'Adithya Kumar\'')
	]
})



'''
main
'''

def best_movies(arg):
	if deny_response(arg):
		return ('401',)
	
	query = build_query({
		'selection': '*',
		'main_tbl': 'Movie',
		'join_tbls': [],
		'criteria': [
			('Movie', 'avg_rating', '>=', 4)
		]
	}) + ' order by avg_rating desc limit 15'

	print query

	return ('200',)

def one_movie(arg):
	if deny_response(arg):
		return ('401',)
	
	id = str(arg['id'])

	'''
	q1 Movie
	q2 People + Roles
	q3 Comments
	'''


	q1 = build_query({
		'selection': '*',
		'main_tbl': 'Movie',
		'join_tbls': [],
		'criteria': [
			('Movie', 'id', '=', id)
		]
	})

	selection = ', '.join([
		'Person.id', 'Person.first_name', 'Person.last_name',
		'Role.id', 'Role.title'
	])
	q2 = build_query({
		'selection': selection,
		'main_tbl': 'Movie_person_role',
		'join_tbls': [
			('inner', ('Person', 'id'), ('Movie_person_role', 'person_id')),
			('inner', ('Role', 'id'), ('Movie_person_role', 'role_id'))
		],
		'criteria': [
			('Movie_person_role', 'movie_id', '=', id)
		]
	})

	q3 = build_query({
		'selection': '*',
		'main_tbl': 'Comment',
		'join_tbls': [],
		'criteria': [
			('Comment', 'movie_id', '=', id)
		]
	})

	print q1
	print q2
	print q3

	return ('200',)


def simple_search(arg):
	if deny_response(arg):
		return ('401',)
	
	search = str(arg['search'])

	query = build_query({
		'selection': '*',
		'main_tbl': 'Movie',
		'join_tbls': [],
		'criteria': [
			('Movie', 'title', 'like', '\'%{}%\''.format(search))
		]
	}) + ' order by avg_rating desc limit 15'

	print query

	return ('200',)










best_movies({
	'resource_req': 'best_movies',
	'requestor': 'admin'
})

one_movie({
	'resource_req': 'best_movies',
	'requestor': 'admin',
	'id': 2
})

simple_search({
	'resource_req': 'best_movies',
	'requestor': 'admin',
	'search': 'iron man'
})