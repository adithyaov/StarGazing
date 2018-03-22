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
	if arg['resource_req'] in arg['valid_resources']:
		return True
	else:
		return False

def build_query(arg):
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
	query_list.append('select * from {main_tbl} as {main_tbl}'.format(main_tbl=main_tbl))

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
	query_list.append('where')
	for (table, column, equality, value) in criteria:
		query_list.append('{}.{} {} {}'.format(table, column, equality, value))

	print query_list


build_query({
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

def get_movies(arg):
	if deny_response(arg):
		return ('401',)
	


	'''
		do something
	'''
	return ('200',)