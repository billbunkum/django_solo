from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	bio = models.TextField(blank=True)
	github_url = models.URLField('')

	def __str__(self):
		return self.name