from django.contrib import admin
from portal.models import posts, category
from django.db import models
from django import forms

class PostsAdmin(admin.ModelAdmin):
    change_form_template = 'portal/admin/change_form.html'
    
# Register your models here.
admin.site.register(posts, PostsAdmin)
admin.site.register(category)