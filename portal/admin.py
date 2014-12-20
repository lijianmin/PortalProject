from django.contrib import admin
from portal.models import post, category, masterCategory, UserProfile
from django.db import models
from django import forms

class PostsAdmin(admin.ModelAdmin):
	#exclude = ['timestamp']
	prepopulated_fields = {"title_slug": ("title",)}
	change_form_template = 'portal/admin/change_form.html'

class CategoryAdmin(admin.ModelAdmin):
	#exclude = ['created_datetime']
	prepopulated_fields = {"category_slug": ("category_name",)}

class MasterCategoryAdmin(admin.ModelAdmin):
	#exclude = ['created_datetime']
	prepopulated_fields = {"master_category_slug": ("master_category_name",)}

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(post, PostsAdmin)
admin.site.register(category, CategoryAdmin)
admin.site.register(masterCategory, MasterCategoryAdmin)