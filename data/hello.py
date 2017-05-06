from pyspark import SparkContext
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

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
count = pages.reduceByKey(lambda x,y: int(x)+int(y))        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for page_id, count in output:
    print ("page_id %s count %d" % (page_id, count))
print ("Popular items done")

sc.stop()
