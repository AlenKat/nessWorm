from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_facebook.models import FacebookCustomUser

# Create your models here.


class Badge(models.Model):
    name = models.CharField('name', max_length=20, unique=True)
    about = models.CharField('about', max_length= 50)
    value = models.IntegerField('value')

    def __unicode__(self):
        return "badge '{0}'".format(self.name)


class Achievment(models.Model):
    state = models.BooleanField('state')
    user = models.ForeignKey(FacebookCustomUser)
    badge = models.ForeignKey('Badge', related_name='badge')

    def __unicode__(self):
        return "Badge: '{0}' : {1}, {2}".format(self.badge.name, self.state, self.user.username)

	def get_absolute_url(self):
		return reverse('badges_list', kwargs = {'name' : self.user})

