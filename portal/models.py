from django.db 						import models
from django.contrib.auth.models 	import User
from django.db.models 				import permalink
from django.template.defaultfilters import slugify

# User Model
class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    country = models.CharField(
    	max_length = 150
    )

    zip_code = models.CharField(
    	max_length = 6
    )

    home_address = models.TextField()

    mobile_no = models.CharField(
    	max_length = 20
    )

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username


# Post Model
class post(models.Model):

	#future article guid variable field
	
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

	view_count = models.IntegerField(
		default = 0
	)
    
	timestamp = models.DateTimeField(
		auto_now_add=True
	)
    
    #strictly one category per post
	category = models.ForeignKey('portal.category')

	#comments_enabled = models.BooleanField(default=False)
	
	def __str__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('view_article', (), { 'slug': self.title_slug, 'id': self.id })
    	
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
		return ('view_category', (), { 'slug': self.category_slug, 'id': self.id })


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