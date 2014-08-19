from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Counter(models.Model):
	badge = models.CharField('badge_name', max_length = 20, unique = True)

	def __unicode__(self):
		return "badge '{0}'".format(self.badge)

class Badge(models.Model):
	value = models.BooleanField('value')
	users = models.ForeignKey(User)
	badges = models.ForeignKey('Counter', related_name = 'badges')

	def __unicode__(self):
		return "Badge: '{0}' : {1}, {2}".format(self.badges.badge, self.value, self.users.username)