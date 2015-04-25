# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20150423_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicianprofile',
            name='clinical_specialty',
            field=models.CharField(choices=[(1, 'Anaethesiology'), (2, 'Cardiology'), (3, 'Cardiothoracic Surgery'), (4, 'Colorectal Surgery'), (5, 'Dentistry'), (6, 'Dermatology'), (7, 'Endocrinology'), (8, 'ENT'), (9, 'Gastroenterology'), (10, 'General Surgery'), (11, 'Geriatrics'), (12, 'Gynaecology'), (13, 'Haematology'), (14, 'Hand Surgery'), (15, 'Infectious Disease'), (16, 'Internal Medicine'), (17, 'Oncology'), (18, 'Neonatology'), (19, 'Neurology'), (20, 'Obstetrics'), (21, 'Ophthalmology'), (22, 'Orthopaedic Surgery'), (23, 'Paediatric'), (24, 'Paediatric Surgery'), (25, 'Plastic Surgery'), (26, 'Psychiatry'), (27, 'Renal Medicine'), (28, 'Respiratory Medicine'), (29, 'Rheumatology'), (30, 'Urology')], max_length=30, default='Anaethesiology'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(choices=[('SG', 'Singapore'), ('MY', 'Malaysia'), ('ID', 'Indonesia'), ('TH', 'Thailand'), ('IN', 'India'), ('VN', 'Vietnam'), ('KOR', 'South Korea, Republic of'), ('AU', 'Australia'), ('NZ', 'New Zealand'), ('PH', 'Philippines'), ('TW', 'Taiwan, Republic of China'), ('CN', 'China, Peoples Republic of'), ('HK', 'Hong Kong SAR, China'), ('MAC', 'Macau SAR, China')], max_length=4, default='SG'),
            preserve_default=True,
        ),
    ]
