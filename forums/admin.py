from django.contrib 	import admin
from forums.models		import Forum, Thread, Post
from django.db 			import models
from django 			import forms

class ForumAdmin(admin.ModelAdmin):
    pass

class ThreadAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
