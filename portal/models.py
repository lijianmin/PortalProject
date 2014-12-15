from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

# Post Model
class post(models.Model):
	
	author = models.CharField(
    	max_length = 30
    )
    
	title = models.CharField(
    	max_length = 150,
    	db_index = True
    )
	
	title_slug = models.SlugField(
    	max_length = 50,
    	db_index = True,
    	unique = True
    )
    
	bodytext = models.TextField()
    
	timestamp = models.DateTimeField(
		auto_now_add=True
	)
    
    #strictly one category per post
	category = models.ForeignKey('portal.category')
    	
	def __str__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('view_article', (), { 'slug': self.title_slug })
    	
	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.title)
		super(post, self).save(*args, **kwargs)
    
# Category Model
class category(models.Model):

	category_name = models.CharField(
		max_length = 100
	)
	
	category_slug = models.SlugField(
		max_length = 100,
		db_index = True,
		unique = True
	)
		
	created_datetime = models.DateTimeField(
		auto_now_add=True
	)

	master_category = models.ForeignKey('portal.masterCategory')

	def __str__(self):
		return self.category_name
	
	def save(self, *args, **kwargs):
		self.category_slug = slugify(self.category_name)
		super(category, self).save(*args, **kwargs)
	
	@models.permalink
	def get_absolute_url(self):
		return ('view_category', (), { 'slug': self.category_slug })

# Master Category
class masterCategory(models.Model):

	master_category_name = models.CharField(
		max_length = 150
	)

	master_category_slug = models.CharField(
		max_length = 150,
		db_index = True
	)

	def __str__(self):
		return self.master_category_name

	def save(self, *args, **kwargs):
		self.master_category_slug = slugify(self.master_category_name)
		super(masterCategory, self).save(*args, **kwargs)
	
	@models.permalink
	def get_absolute_url(self):
		return ('view_master_category', (), { 'slug': self.master_category_slug })