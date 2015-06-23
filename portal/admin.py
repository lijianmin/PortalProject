from django.contrib 	import admin
from portal.models 		import article, category, masterCategory, condition
from django.db 			import models
from django 			import forms

class ArticlesAdmin(admin.ModelAdmin):
	#exclude = ['timestamp']
	prepopulated_fields = {"title_slug": ("title",)}
	change_form_template = 'portal/admin/change_form.html'
	readonly_fields = ('article_UUID',)

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

	def save_formset(self, request, form, formset, change):
		if formset.model == post:
			instances = formset.save(commit=False)
			for instance in instances:
				instance.author = request.user
				instance.save()
		else:
			formset.save()

class ConditionAdmin(admin.ModelAdmin):

	prepopulated_fields = {"name_slug": ("name",)}
	readonly_fields = ('condition_UUID',)

class CategoryAdmin(admin.ModelAdmin):
	#exclude = ['created_datetime']
	prepopulated_fields = {"category_slug": ("category_name",)}

class MasterCategoryAdmin(admin.ModelAdmin):
	#exclude = ['created_datetime']
	prepopulated_fields = {"master_category_slug": ("master_category_name",)}

# Register your models here.
admin.site.register(article, ArticlesAdmin)
admin.site.register(category, CategoryAdmin)
admin.site.register(masterCategory, MasterCategoryAdmin)
admin.site.register(condition, ConditionAdmin)
