from django.contrib import admin
from worm.models import Counter, Badge

# class AdminPost(admin.ModelAdmin):
# 	fields = ['content']

# Register your models here.
admin.site.register(Counter)
admin.site.register(Badge)