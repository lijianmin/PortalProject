from django.db 						import models
from profile.models					import User
from django.db.models 				import permalink
from django.template.defaultfilters import slugify
from django_extensions.db.fields 	import UUIDField
from taggit.managers                import TaggableManager
from django.conf                    import settings

# two-factor authentication - explore that option by utilising a service
# spruce up the forums

# Post Model -- Articles mainly...yea
class post(models.Model):

    tags = TaggableManager()

	# Article UUID - internal to the portal only.
    article_UUID = UUIDField(blank=True, null=True)

    author = models.ForeignKey(User)

    title = models.CharField(
    	max_length = 200,
    	db_index = True
    )

    title_slug = models.SlugField(
    	max_length = 200,
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

	#enable/disable the Disqus comments system (per article via the admin)
    comments_enabled = models.BooleanField(default=False)

	#publish when you are confident enough
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_article', (), { 'slug': self.title_slug, 'id': self.id })

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)

from django.db.models.signals 		import pre_save
from portal.signals					import create_redirect

pre_save.connect(create_redirect, sender=post, dispatch_uid="001")

class condition(models.Model):

    # Condition under Category
    category = models.ForeignKey('portal.category')

    name = models.CharField(unique=True, max_length=250, db_index=True)

    name_slug = models.SlugField(
    	max_length = 200,
    )

    tags = TaggableManager()

    condition_UUID = UUIDField(blank=True, null=True)

    overview = models.TextField()

    transmission = models.TextField()

    symptoms = models.TextField()

    complications = models.TextField()

    diagnosis = models.TextField()

    treatment = models.TextField()

    prevention = models.TextField()

    #publish when you are confident enough
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(condition, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('view_condition', (), { 'slug': self.name_slug, 'id': self.id })

    class Meta:
        verbose_name_plural = 'Conditions'


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

	definition = models.TextField(blank=True)

	def __str__(self):
		return self.category_name

	def save(self, *args, **kwargs):
		self.category_slug = slugify(self.category_name)
		super(category, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ('view_category', (), { 'slug': self.category_slug, 'id': self.id })

	class Meta:
		verbose_name_plural = 'Categories'

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
		return ('view_master_category', (), { 'slug': self.master_category_slug, 'id': self.id })

	class Meta:
		verbose_name_plural = 'Master Categories'
