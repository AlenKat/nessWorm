from django.shortcuts import render, HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, TemplateView
from worm.models import Counter, Badge
from django_facebook.models import FacebookCustomUser
from open_facebook import OpenFacebook

# Create your views here.
# def view_all(request):
# 	return HttpResponse('Hello')


class BadgeUserListView(ListView):
    model = Badge
    template_name = 'badges.html'

    def get_queryset(self):
        self.name = self.kwargs['name']

    def get_context_data(self, **kwargs):
        context = super(BadgeUserListView, self).get_context_data(**kwargs)
        context['badges'] = Badge.objects.filter(user=FacebookCustomUser.objects.filter(username=self.name))
        return context


class Connect(TemplateView):
    template_name = 'connect.html'




