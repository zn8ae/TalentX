from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 200, default="", primary_key=True)
	first_name = models.CharField(max_length = 100, default="")
	last_name = models.CharField(max_length = 100, default="")
	title = models.CharField(max_length = 100, blank=True)
	company = models.CharField(max_length = 200, blank=True)
	phone = models.CharField(max_length = 200, blank=True)
	email = models.EmailField(max_length=254, default="")

class Mission(models.Model):
	#pk of user who has this Mission
	username = models.CharField(max_length = 200, default="")
	mname = models.CharField(max_length = 200)
	desc = models.CharField(max_length = 200, blank=True)
	# Price should be decimals? Yes there is Decimalfield
	price = models.IntegerField(default=0)

class Skill(models.Model):
	username = models.CharField(max_length = 200, default="")
	sname = models.CharField(max_length = 200)
	desc = models.CharField(max_length = 200, blank=True)
	price = models.DecimalField(max_digits=9, decimal_places=2)

class Account(models.Model):
	username = models.CharField(max_length = 200, default="")
	password = models.CharField(max_length = 300, default="")
	
class Authenticator(models.Model):
	username = models.CharField(max_length = 200, default="")
	authenticator = models.CharField(max_length = 300, default="")
	date_created = models.CharField(max_length = 100, default="")