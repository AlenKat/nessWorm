from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Counter(models.Model):
	name = models.CharField('name', max_length = 20, unique = True)

	def __unicode__(self):
		return "badge '{0}'".format(self.name)

class Badge(models.Model):
	value = models.BooleanField('value')
	user = models.ForeignKey(User)
	counter = models.ForeignKey('Counter', related_name = 'counter')

	def __unicode__(self):
		return "Badge: '{0}' : {1}, {2}".format(self.counter.name, self.value, self.user.username)