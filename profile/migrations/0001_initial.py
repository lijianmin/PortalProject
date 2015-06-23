# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
#import spirit.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                #('slug', spirit.utils.models.AutoSlugField(blank=True, populate_from='username', db_index=False)),
                ('location', models.CharField(blank=True, verbose_name='location', max_length=75)),
                ('last_seen', models.DateTimeField(verbose_name='last seen', auto_now=True)),
                ('last_ip', models.GenericIPAddressField(blank=True, verbose_name='last ip', null=True)),
                ('timezone', models.CharField(choices=[('Etc/GMT+12', '(GMT -12:00) Eniwetok, Kwajalein'), ('Etc/GMT+11', '(GMT -11:00) Midway Island, Samoa'), ('Etc/GMT+10', '(GMT -10:00) Hawaii'), ('Pacific/Marquesas', '(GMT -9:30) Marquesas Islands'), ('Etc/GMT+9', '(GMT -9:00) Alaska'), ('Etc/GMT+8', '(GMT -8:00) Pacific Time (US & Canada)'), ('Etc/GMT+7', '(GMT -7:00) Mountain Time (US & Canada)'), ('Etc/GMT+6', '(GMT -6:00) Central Time (US & Canada), Mexico City'), ('Etc/GMT+5', '(GMT -5:00) Eastern Time (US & Canada), Bogota, Lima'), ('America/Caracas', '(GMT -4:30) Venezuela'), ('Etc/GMT+4', '(GMT -4:00) Atlantic Time (Canada), Caracas, La Paz'), ('Etc/GMT+3', '(GMT -3:00) Brazil, Buenos Aires, Georgetown'), ('Etc/GMT+2', '(GMT -2:00) Mid-Atlantic'), ('Etc/GMT+1', '(GMT -1:00) Azores, Cape Verde Islands'), ('UTC', '(GMT) Western Europe Time, London, Lisbon, Casablanca'), ('Etc/GMT-1', '(GMT +1:00) Brussels, Copenhagen, Madrid, Paris'), ('Etc/GMT-2', '(GMT +2:00) Kaliningrad, South Africa'), ('Etc/GMT-3', '(GMT +3:00) Baghdad, Riyadh, Moscow, St. Petersburg'), ('Etc/GMT-4', '(GMT +4:00) Abu Dhabi, Muscat, Baku, Tbilisi'), ('Asia/Kabul', '(GMT +4:30) Afghanistan'), ('Etc/GMT-5', '(GMT +5:00) Ekaterinburg, Islamabad, Karachi, Tashkent'), ('Asia/Kolkata', '(GMT +5:30) India, Sri Lanka'), ('Asia/Kathmandu', '(GMT +5:45) Nepal'), ('Etc/GMT-6', '(GMT +6:00) Almaty, Dhaka, Colombo'), ('Indian/Cocos', '(GMT +6:30) Cocos Islands, Myanmar'), ('Etc/GMT-7', '(GMT +7:00) Bangkok, Hanoi, Jakarta'), ('Etc/GMT-8', '(GMT +8:00) Beijing, Perth, Singapore, Hong Kong'), ('Australia/Eucla', '(GMT +8:45) Australia (Eucla)'), ('Etc/GMT-9', '(GMT +9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk'), ('Australia/North', '(GMT +9:30) Australia (Northern Territory)'), ('Etc/GMT-10', '(GMT +10:00) Eastern Australia, Guam, Vladivostok'), ('Etc/GMT-11', '(GMT +11:00) Magadan, Solomon Islands, New Caledonia'), ('Pacific/Norfolk', '(GMT +11:30) Norfolk Island'), ('Etc/GMT-12', '(GMT +12:00) Auckland, Wellington, Fiji, Kamchatka')], verbose_name='time zone', default='UTC', max_length=32)),
                ('is_administrator', models.BooleanField(verbose_name='administrator status', default=False)),
                ('is_moderator', models.BooleanField(verbose_name='moderator status', default=False)),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified', help_text='Designates whether the user has verified his account by email or by other means. Un-select this to let the user activate his account.')),
                ('topic_count', models.PositiveIntegerField(verbose_name='topic count', default=0)),
                ('comment_count', models.PositiveIntegerField(verbose_name='comment count', default=0)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email Address', db_index=True)),
                ('username', models.CharField(unique=True, verbose_name='User Name', max_length=30)),
                ('first_name', models.CharField(blank=True, verbose_name='First Name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='Last Name', max_length=30)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined', default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set', related_query_name='user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClinicianProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('medical_reg_no', models.CharField(max_length=9)),
                ('registered_date', models.DateTimeField(null=True)),
                ('practice_address', models.TextField()),
                ('practice_contact_no', models.CharField(max_length=20)),
                ('practice_country', models.CharField(max_length=200)),
                ('practice_website', models.URLField()),
                ('practice_email_add', models.EmailField(max_length=75)),
                ('practice_gps_coord', models.CharField(max_length=20)),
                ('clinical_specialty', models.IntegerField(choices=[(1, 'Anaethesiology'), (2, 'Cardiology'), (3, 'Cardiothoracic Surgery'), (4, 'Colorectal Surgery'), (5, 'Dentistry'), (6, 'Dermatology'), (7, 'Endocrinology'), (8, 'ENT'), (9, 'Gastroenterology'), (10, 'General Surgery'), (11, 'Geriatrics'), (12, 'Gynaecology'), (13, 'Haematology'), (14, 'Hand Surgery'), (15, 'Infectious Disease'), (16, 'Internal Medicine'), (17, 'Oncology'), (18, 'Neonatology'), (19, 'Neurology'), (20, 'Obstetrics'), (21, 'Ophthalmology'), (22, 'Orthopaedic Surgery'), (23, 'Paediatric'), (24, 'Paediatric Surgery'), (25, 'Plastic Surgery'), (26, 'Psychiatry'), (27, 'Renal Medicine'), (28, 'Respiratory Medicine'), (29, 'Rheumatology'), (30, 'Urology')], default=1)),
                ('medical_interests', models.TextField()),
                ('grad_school', models.CharField(max_length=200)),
                ('grad_year', models.CharField(max_length=4)),
                ('degree_type', models.CharField(max_length=7)),
                ('writeup_text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicUserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('allergies', models.TextField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('country', models.CharField(choices=[('SG', 'Singapore'), ('MY', 'Malaysia'), ('ID', 'Indonesia'), ('TH', 'Thailand'), ('IN', 'India'), ('VN', 'Vietnam'), ('KOR', 'South Korea, Republic of'), ('AU', 'Australia'), ('NZ', 'New Zealand'), ('PH', 'Philippines'), ('TW', 'Taiwan, Republic of China'), ('CN', 'China, Peoples Republic of'), ('HK', 'Hong Kong SAR, China'), ('MAC', 'Macau SAR, China')], default='SG', max_length=4)),
                ('gender', models.CharField(choices=[('M', 'Female'), ('F', 'Male'), ('UN', 'Unknown')], default='F', max_length=2)),
                ('zip_code', models.CharField(max_length=6)),
                ('birthday', models.DateTimeField(null=True)),
                ('posts', models.IntegerField(default=0)),
                ('home_address', models.TextField()),
                ('avatar', models.ImageField(upload_to='images/', blank=True, verbose_name='Profile Pic', null=True)),
                ('mobile_no', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publicuserprofile',
            name='userprofile',
            field=models.OneToOneField(to='profile.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinicianprofile',
            name='userprofile',
            field=models.OneToOneField(to='profile.UserProfile'),
            preserve_default=True,
        ),
    ]
