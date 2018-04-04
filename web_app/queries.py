'''
Functions:

movie
movies

Person

advance search

user system
can comment
can upvote/downvote
can rate


'''

'''
helpers
'''

def deny_response(arg):
	return False

def format_value(value):
	try:
		int(value)
		return str(value)
	except:
		pass

	try:
		float(value)
		return str(value)
	except:
		pass

	return '"{}"'.format(value)
	

def recurse_criteria(criteria, query_list):
	new_list = query_list
	if type(criteria) == type([]):
		criteria = ('and', criteria)
	for x in criteria[1]:
		if len(x) == 2:
			new_list.append('(')
			new_list = new_list + recurse_criteria(x, [])
			new_list.append(')')
		else:
			(table, column, equality, value) = x
			value = format_value(value)
			new_list.append('{}.{} {} {}'.format(table, column, equality, value))
		new_list.append(criteria[0])
	return new_list[:-1]


def read_query(arg):
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
		query_list = query_list + recurse_criteria(criteria, [])

	return ' '.join(query_list)




def insert_query(arg):
	table = arg['table']
	k_list = arg['k_list']
	v_list = arg['v_list']

	query_list = []
	query_list.append('insert into {}'.format(table))
	
	if len(k_list) > 0:
		query_list.append('(')
		query_list.append(', '.join(k_list))
		query_list.append(')')

	query_list.append('values')

	query_list.append('(')
	query_list.append(', '.join([format_value(v) for v in v_list]))
	query_list.append(')')

	return ' '.join(query_list)


def update_query(arg):
	table = arg['table']
	update_tuples = arg['update_tuples']
	criteria = arg['criteria']

	query_list = []
	query_list.append('update {} set'.format(table))

	query_list.append(', '.join(['{} = {}'.format(c, format_value(v)) for (c, v) in update_tuples]))

	if len(criteria) > 0:
		query_list.append('where')
		query_list = query_list + recurse_criteria(criteria, [])


	return ' '.join(query_list)


def delete_query(arg):
	table = arg['table']
	criteria = arg['criteria']

	query_list = []
	query_list.append('delete from {}'.format(table))
	
	if len(criteria) > 0:
		query_list.append('where')
		query_list = query_list + recurse_criteria(criteria, [])

	return ' '.join(query_list)


'''
main
'''

def best_movies():
	
	query = read_query({
		'selection': '*',
		'main_tbl': 'Movie',
		'join_tbls': [],
		'criteria': [
			('Movie', 'avg_rating', '>=', '4')
		]
	}) + ' order by avg_rating desc limit 15'

	print query

	return ('200', query)

def one_movie(arg):
	
	id = arg['id']

	'''
	q1 Movie
	q2 People + Roles
	q3 Comments
	'''


	q1 = read_query({
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
	q2 = read_query({
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

	q3 = read_query({
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

	return ('200', [q1, q2, q3])


def simple_movie_search(arg):
	
	search = arg['search']

	query = read_query({
		'selection': '*',
		'main_tbl': 'Movie',
		'join_tbls': [],
		'criteria': [
			('Movie', 'title', 'like', '\'%{}%\''.format(search))
		]
	}) + ' order by avg_rating desc limit 15'

	print query

	return ('200',)

def simple_person_search(arg):
	
	search = arg['search']

	query = read_query({
		'selection': '*',
		'main_tbl': 'Person',
		'join_tbls': [],
		'criteria': ('or', [
					('Person', 'first_name', 'like', '\'%{}%\''.format(search)),
					('Person', 'last_name', 'like', '\'%{}%\''.format(search))
				])
	}) + ' limit 15'

	print query

	return ('200',)


def one_person(arg):
	id = arg['id']
	q1 = read_query({
		'selection': '*',
		'main_tbl': 'Person',
		'join_tbls': [],
		'criteria': [
			('Person', 'id', '=', id)
		]
	})

	selection = ', '.join([
		'Movie.id', 'Movie.title', 'Movie.avg_rating',
		'Role.id', 'Role.title'
	])
	q2 = read_query({
		'selection': selection,
		'main_tbl': 'Movie_person_role',
		'join_tbls': [
			('inner', ('Movie', 'id'), ('Movie_person_role', 'movie_id')),
			('inner', ('Role', 'id'), ('Movie_person_role', 'role_id'))
		],
		'criteria': [
			('Movie_person_role', 'person_id', '=', id)
		]
	})

	print q1
	print q2

	return (200, [q1, q2])






one_person({
	'resource_req': 'best_movies',
	'requestor': 'admin',
	'id': '2'
})