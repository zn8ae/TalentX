##This is my Django MySQL based marketplace website.


The website now has 3-layer applications: Web, Exp, Model

The website has a homepage and a profile page.

The web front-end will call exp service which would call multiple entity APIs and combine them into a Json and return it.

The web front-end then use the Json from exp service to render content.

Rendered content include the username, hottest mission on the front page, and the user profile, user missions on the profile page.

---------------------------------------
Database contains an User table and a Mission table.

You can call APIs to create, lookup, delete and update user and mission.

Examples:

To create an user, make a POST request with parameter uname such as http://localhost:8001/users/create with param uname, first_name, last_name, email

To lookup an user, make a GET request with user id such as http://localhost:8001/users/1

To update an user, make a POST request with parameter id and uname such as http://localhost:8001/users/update with param id=1 and uname, first_name, last_name, title, email, company, phone

To delete an user, make a POST request with parameter id such as http://localhost:8001/users/delete with param id=1

