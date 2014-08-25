from django.contrib import admin
from worm.models import Badge, Achievment

# class AdminPost(admin.ModelAdmin):
# 	fields = ['content']

# Register your models here.
admin.site.register(Badge)
admin.site.register(Achievment)