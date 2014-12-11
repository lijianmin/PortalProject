from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class posts(models.Model):
	
	author = models.CharField(
    	max_length = 30
    )
    
	title = models.CharField(
    	max_length = 150,
    	db_index = True
    )
	
	title_slug = models.SlugField(
    	max_length = 50,
    	db_index = True
    )
    
	bodytext = models.TextField()
    
	timestamp = models.DateTimeField()
    
	category = models.ForeignKey('portal.category')
    	
	def __str__(self):
		return self.title
    
	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.title)
		super(posts, self).save(*args, **kwargs)
    
class category(models.Model):

	category_name = models.CharField(
		max_length = 100
	)
	
	created_datetime = models.DateTimeField()

	def __str__(self):
		return self.category_name
