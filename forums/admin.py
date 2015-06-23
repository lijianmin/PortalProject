from django.contrib 	import admin
from forums.models		import Forum, Thread, Post
from django.db 			import models
from django 			import forms

class ForumAdmin(admin.ModelAdmin):
    pass

class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "thread", "creator", "created"]

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
