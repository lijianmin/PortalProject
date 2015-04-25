from django.db 						import models
from django.contrib.auth.models 	import User
from django.db.models 				import permalink
from django.template.defaultfilters import slugify
from django_extensions.db.fields 	import UUIDField
from taggit.managers                import TaggableManager

# from PIL 							import Image as PImage
# from os.path 						import join as pjoin

# two-factor authentication - explore that option by utilising a service
# spruce up the forums


# User Model for All Users only. - biggest regret to put it in the portal app :(
class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    country = (
        ('SG','Singapore'),
        ('MY','Malaysia'),
        ('ID','Indonesia'),
        ('TH','Thailand'),
        ('IN','India'),
        ('VN','Vietnam'),
        ('KOR','South Korea, Republic of'),
        ('AU','Australia'),
        ('NZ','New Zealand'),
        ('PH','Philippines'),
        ('TW','Taiwan, Republic of China'),
        ('CN','China, People''s Republic of'),
        ('HK','Hong Kong SAR, China'),
        ('MAC','Macau SAR, China')
    )
    country = models.CharField(
        max_length = 4, choices = country, default='SG'
    )

    gender = (
        ('M', 'Female'),
        ('F', 'Male'),
        ('UN', 'Unknown'),
    )

    gender = models.CharField(
        max_length = 2, choices = gender, default='F'
    )

    # The additional attributes we wish to include.

    zip_code = models.CharField(
    	max_length = 6
    )

    # type of user: either clinician, pharmacist or general user ex. admin

    # profile_avatar = models.ImageField("Profile Pic", upload )

    birthday = models.DateTimeField(null=True)

    posts = models.IntegerField(default = 0)

    home_address = models.TextField()

    avatar = models.ImageField("Profile Pic", upload_to='images/', blank=True, null=True)

    mobile_no = models.CharField(
    	max_length = 20
    )

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

# User Model for Clinician - with some common features from the UserProfile class
class ClinicianProfile(models.Model):

    userprofile = models.OneToOneField(UserProfile)

    specialty_choices = (
        (1, 'Anaethesiology'),
        (2, 'Cardiology'),
        (3, 'Cardiothoracic Surgery'),
        (4, 'Colorectal Surgery'),
        (5, 'Dentistry'),
        (6, 'Dermatology'),
        (7, 'Endocrinology'),
        (8, 'ENT'),
        (9, 'Gastroenterology'),
        (10, 'General Surgery'),
        (11, 'Geriatrics'),
        (12, 'Gynaecology'),
        (13, 'Haematology'),
        (14, 'Hand Surgery'),
        (15, 'Infectious Disease'),
        (16, 'Internal Medicine'),
        (17, 'Oncology'),
        (18, 'Neonatology'),
        (19, 'Neurology'),
        (20, 'Obstetrics'),
        (21, 'Ophthalmology'),
        (22, 'Orthopaedic Surgery'),
        (23, 'Paediatric'),
        (24, 'Paediatric Surgery'),
        (25, 'Plastic Surgery'),
        (26, 'Psychiatry'),
        (27, 'Renal Medicine'),
        (28, 'Respiratory Medicine'),
        (29, 'Rheumatology'),
        (30, 'Urology')
    )

    # Available fields: medical_reg_no, registered_date, practice_address,
    # practice_contact_no, practice_country, practice_website,
    # practice_email_add, clinical_specialty, medical_interests, grad_school,
    # grad_year, degree_type, writeup_text

    # Professional License
    # for SG: SMC MCR Number
    medical_reg_no = models.CharField(
        max_length = 9
    )

    registered_date = models.DateTimeField(null=True)

    # Clinic of Practice
    # Place of practice e.g. Family Care Clinic
    practice_address = models.TextField()

    # Contact no. of practice
    practice_contact_no = models.CharField(
        max_length = 20
    )

    # Country of practice
    practice_country = models.CharField(
        max_length = 200
    )

    # Website URL of practice
    practice_website = models.URLField()
    practice_email_add = models.EmailField()

    # Place of practice coordinates for use with Google Maps.
    practice_gps_coord = models.CharField(
        max_length = 20
    )

    # to be semi colon separated
    clinical_specialty = models.IntegerField(choices = specialty_choices, default=1)
    medical_interests = models.TextField()

    # Graduate School
    grad_school = models.CharField(
        max_length = 200
    )

    grad_year = models.CharField(
        max_length = 4
    )

    degree_type = models.CharField(
        max_length = 7
    )

    # text profile of clinician
    writeup_text = models.TextField()


# User Model for User - with some common features from the UserProfile class
class PublicUserProfile(models.Model):

    #More to be added. E.g. various medical related data
    userprofile = models.OneToOneField(UserProfile)

    #Semi-colon separated field
    allergies = models.TextField()

    height = models.FloatField()

    weight = models.FloatField()



# Post Model -- Articles mainly...yea
class post(models.Model):

    tags = TaggableManager()

	# Article UUID - internal to the portal only.
    article_UUID = UUIDField(blank=True, null=True)

    author = models.CharField(
    	max_length = 30
    )

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
		return ('view_master_category', (), { 'slug': self.master_category_slug })

	class Meta:
		verbose_name_plural = 'Master Categories'
