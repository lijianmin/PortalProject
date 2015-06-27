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

    avatar = models.ImageField("Profile Pic", upload_to='images/avatars/', blank=True, null=True)

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

    # to be semi colon separated
    clinical_specialty = models.IntegerField(choices = specialty_choices, default=1)

    # semi-colon delimited
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
