from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.

class Student(models.Model):
	username = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=250)
	country = models.CharField(max_length=15)
	dob = models.DateField(default=date.today)
	address = models.TextField()
	country = models.CharField(max_length=50)
	about = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.firstname

	def __unicode__(self):
		return self.firstname

	class Meta:
		ordering = ["-timestamp"]


class Course(models.Model):
	pass