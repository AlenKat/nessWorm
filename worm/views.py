from django.shortcuts import render, render_to_response, HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, TemplateView
from worm.models import Badge, Achievment, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_facebook.models import FacebookCustomUser
from open_facebook import OpenFacebook

# Create your views here.
# def view_all(request):
# 	return HttpResponse('Hello')
class Home(TemplateView):
	template_name = 'home.html'

# class BadgeUserListView(ListView):
# 	model = Badge
# 	template_name = 'badges.html'
# 	badges = []
# 	paginate_by = 6

# 	# def get_queryset(self):
# 	# 	self.name = self.kwargs['name']2
# 	def get_context_data(self, **kwargs):
# 		user = User.objects.filter(username = 'john')
# 		context = super(BadgeUserListView, self).get_context_data(**kwargs)
# 		#context['badges'] = Badge.objects.all() #Badge.objects.filter(user = user)
# 		self.model = Badge.objects.filter(user = 3) #context['badges']
# 		return context


def listing(request):
	badges_list = Achievment.objects.filter(user=FacebookCustomUser.objects.filter(username="katarina"))
	paginator = Paginator(badges_list, 3)

	page = request.GET.get('page')
	try:
		badges = paginator.page(page)
	except PageNotAnInteger:
		badges = paginator.page(1)
	except EmptyPage:
		badges = paginator.page(paginator.num_pages)

	return render_to_response('badges.html', {"badges": badges})


class AboutGame(TemplateView):
	template_name = 'about.html'

class Contact(TemplateView):
	template_name = 'contact.html'

class LogIn(TemplateView):
	template_name = 'login.html'

class Connect(TemplateView):
    template_name = 'connect.html'



