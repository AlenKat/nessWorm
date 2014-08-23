from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from worm import views
admin.autodiscover()

urlpatterns = patterns('worm.views',
    # Examples:
    # url(r'^$', 'NESSproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'/hello', 'view_all'),
    # url(r'/list/(?P<name>.+)$', views.BadgeUserListView.as_view(), name = 'badge_list'),
    url(r'^/list/(?P<name>.+)$', views.BadgeUserListView.as_view(), name='badges_list'),
    url(r'^/connect', views.Connect.as_view()),
)
