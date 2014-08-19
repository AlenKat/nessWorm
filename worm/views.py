from django.shortcuts import render, HttpResponse
from worm.models import Counter, Badge

# Create your views here.
# def view_all(request):
# 	return HttpResponse('Hello')

def view_all_badges(request):
	badges_name = Counter.objects.all()
	print badges_name
	return render(request, "badges.html", {'badges_name' : badges_name})