from pyspark import SparkContext
import itertools
import MySQLdb


# Open database connection
db = MySQLdb.connect(host="db",passwd="$3cureUS",db="cs4501")
# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
	# Prepare SQL query to INSERT a record into the database.
	sql = "delete from users_recommendations where id > 0;"
	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()

# map reduce
sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: tuple(line.split("\t")))


output = pairs.collect()
print("Initial Data")
for user, page in output:
	print("user: %s, page: %s" % (user, page))


distinct_pairs = pairs.distinct()
output = distinct_pairs.collect()
print("Distinct Pairs")
for user, page in output:
	print("user: %s, page: %s" % (user, page))


user_pages = distinct_pairs.groupByKey().mapValues(lambda pages: sorted(pages))
output = user_pages.collect()
print("Group by user, sorted.")
for user, pages in output:
	print("user: %s, pages: %s" % (user, list(pages)))


user_pairs = user_pages.flatMapValues(lambda user_pages: itertools.combinations(user_pages, 2))
output = user_pairs.collect()
print("Pages Pairs for Users")
for user, pair in output:
	print("user: %s, page pairs: %s" % (user, pair))


reverse_user_pairs = user_pairs.map(lambda user_pair: (user_pair[1], user_pair[0]))
output = reverse_user_pairs.collect()
print("Reversed User Pairs")
for pair, user in output:
	print("pair: %s, user: %s" % (pair, user))


grouped_pairs = reverse_user_pairs.groupByKey()
output = grouped_pairs.collect()
print("Grouped Pairs for all users")
for pair, users in output:
	print("pair: %s, users: %s" % (pair, list(users)))


pair_counts = grouped_pairs.map(lambda pair: (pair[0], len(pair[1])))
output = pair_counts.collect()
print("Count Pairs")
for pair, count in output:
	print("pair: %s, count: %s" % (pair, count))


significant_pairs = pair_counts.filter(lambda pair: pair[1] > 2)
output = significant_pairs.collect()
print("Pairs with 3 or more user")
for pair, count in output:
	print("pair: %s, count: %s" % (pair, count))

#need to do one more map-reduce to group pairs by 


sc.stop()




