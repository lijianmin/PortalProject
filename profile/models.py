from django.db                  import models
from django.utils               import timezone
from django.utils.http          import urlquote
from django.utils.translation   import ugettext_lazy as _
from django.core.mail           import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf                import settings

import datetime

class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email       = models.EmailField('Email Address', max_length=254, unique=True, db_index=True)

    username    = models.CharField('User Name', max_length=30, unique=True)

    first_name  = models.CharField('First Name', max_length=30, blank=True)

    last_name   = models.CharField('Last Name', max_length=30, blank=True)

    initial     = models.CharField('Initial', max_length=4, blank=True)

    is_staff    = models.BooleanField('Staff status', default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))

    is_active   = models.BooleanField('Active', default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    is_admin    = models.BooleanField(default=False)

    date_joined = models.DateTimeField('Date joined', default=timezone.now)

    objects     = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    activation_key = models.CharField(max_length=40, blank=True)

    key_expires = models.DateTimeField(default=datetime.date.today())

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

    birthday = models.DateTimeField(null=True)

    posts = models.IntegerField(default = 0)

    home_address = models.TextField()

    avatar = models.ImageField("Profile Pic", upload_to='avatars/', blank=True, null=True)

    mobile_no = models.CharField(
    	max_length = 20
    )


class Clinic(models.Model):

    # Clinic of Practice
    name = models.CharField('Clinic Name', max_length=254, unique=True)

    # Place of practice e.g. Family Care Clinic
    address = models.TextField()

    # Contact no. of practice
    contact_no = models.CharField(
        max_length = 20
    )

    # Country of practice
    country = models.CharField(
        max_length = 200
    )

    # Website URL of practice
    website = models.URLField('Business Website')

    # Business Email Address for Contact
    business_email_address = models.EmailField('Business Email Address', max_length=254, db_index=True)

    # Place of practice coordinates for use with Google Maps.
    gps_coord = models.CharField(
        max_length = 20
    )

    # Business Registration Date
    business_registered_date = models.DateTimeField('Business Registration Date', null=True)

    # Services in semi-colon delimited fashion
    services = models.TextField('Provided Services')

# User Model for Clinician - with some common features from the UserProfile class
class ClinicianProfile(models.Model):

    """
    - My Education (institutions)(from yyyy - yyyy) provide 3 rows and allow to add *Do It Later*
    - My Medical Training (hospital)(from yyyy - yyyy) provide 3 rows and allow to add *Do It Later*
    """

    userprofile = models.OneToOneField(UserProfile)

    clinic_of_practice = models.ForeignKey(Clinic, default=1)

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

    medical_careergrade_choices = (
        (1, 'Medical Officer'),
        (2, 'Senior Medical Officer'),
        (3, 'Registrar'),
        (4, 'Associate Consultant'),
        (5, 'Consultant'),
        (6, 'Senior Consultant'),
        (7, 'Family Physician'),
        (8, 'Family Physician Associate Consultant'),
        (9, 'Family Physician Consultant'),
        (10, 'Family Physician Senior Consultant'),
        (11, 'Resident'),
        (12, 'Senior Resident'),
        (13, 'Principal Resident')
    )

    # Professional License
    # for SG: SMC MCR Number
    medical_reg_no = models.CharField(
        max_length = 9
    )

    registered_date = models.DateTimeField(null=True)

    clinical_specialty = models.IntegerField(choices = specialty_choices, default=1)

    medical_careergrade = models.IntegerField(choices = medical_careergrade_choices, default=1)

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

    years_of_practice = models.IntegerField(default=0)

    # Free Text Fields
    # text profile of clinician - about me
    medical_interests = models.TextField(default="")
    writeup_text = models.TextField(default="")
    medical_memberships = models.TextField(default="")
    publications = models.TextField(default="")
    affiliations = models.TextField(default="")
    awards = models.TextField(default="")

# User Model for User - with some common features from the UserProfile class
class PublicUserProfile(models.Model):

    #More to be added. E.g. various medical related data
    userprofile = models.OneToOneField(UserProfile)

    race = models.CharField(max_length=100, default="")

    sexual_history_options = ((1, 'Not Sexually Active'),(2, 'Homosexual'),(3, 'Heterosexual'),(4, 'Bisexual'))
    sexual_history = models.IntegerField(choices = sexual_history_options, default=1)

    current_medical_conditions = models.TextField(default="")

    lactose_intolerant_options = ((1,'Yes'),(2,'No'))
    lactose_intolerant = models.IntegerField(choices = lactose_intolerant_options, default=1)

    smoking_options = ((1,'Yes'),(2,'No'))
    smoking = models.IntegerField(choices = smoking_options, default=1)
    smoking_packs = models.CharField(max_length = 4, default=0)
    smoking_years = models.CharField(max_length = 4, default=0)

    alcohol_intake_options = ((1, 'None'),(2,'<7 drinks a week'),(3,'8-14 drinks a week'),(4,'>15 drinks a week'))
    alcohol_intake = models.IntegerField(choices = alcohol_intake_options, default=1)

    relative_cancer_options = ((1,'None'),(2,'Grandfather'),(3,'Grandmother'),(4,'Father'),(5,'Mother'),(6,'Sibling'))
    relative_with_cancer = models.IntegerField(choices = relative_cancer_options, default=1)
    cancer_desc = models.TextField(default="")

    allergies = models.TextField(default="")

    height = models.FloatField()
    weight = models.FloatField()
