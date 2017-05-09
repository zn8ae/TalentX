Docker-compose up will start spark-master and spark-worker and install dependencies into each container and prepare the web application containers.

runner.sh will automate spark map-reduce job to produce recommendation table in the interval of 60 seconds and inject the newly produced table into database.

Everytime a user clicks the item detail page, a record will be written to access.log for future recommendation usage. In the item detail page, the recommendations (co-view items) will be displayed according to database. If this item does not have co-view items, no recommeneded item will be displayed. 