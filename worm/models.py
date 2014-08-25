from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_facebook.models import FacebookCustomUser

# Create your models here.


class Counter(models.Model):
    name = models.CharField('name', max_length=20, unique=True)

    def __unicode__(self):
        return "badge '{0}'".format(self.name)


class Badge(models.Model):
    value = models.BooleanField('value')
    user = models.ForeignKey(FacebookCustomUser)
    counter = models.ForeignKey('Counter', related_name='counter')

    def __unicode__(self):
        return "Badge: '{0}' : {1}, {2}".format(self.counter.name, self.value, self.user.username)

	def get_absolute_url(self):
		return reverse('badges_list', kwargs = {'name' : self.user})

