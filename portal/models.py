from django.db import models

# Create your models here.
class posts(models.Model):
    author = models.CharField(
    	max_length = 30
    )
    
    title = models.CharField(
    	max_length = 100
    )
    
    bodytext = models.TextField()
    
    timestamp = models.DateTimeField()
    
    #hashtag = models.TextField()
    
    #category = models.CharField(max_length = 100)
    
    def __str__(self):
    	return self.title
    
class category(models.Model):
	category_name = models.CharField(
		max_length = 100
	)
	
	created_datetime = models.DateTimeField()
	
	def __str__(self):
		return self.category_name
