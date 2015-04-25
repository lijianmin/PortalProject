# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20150423_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicianprofile',
            name='clinical_specialty',
            field=models.IntegerField(choices=[(1, 'Anaethesiology'), (2, 'Cardiology'), (3, 'Cardiothoracic Surgery'), (4, 'Colorectal Surgery'), (5, 'Dentistry'), (6, 'Dermatology'), (7, 'Endocrinology'), (8, 'ENT'), (9, 'Gastroenterology'), (10, 'General Surgery'), (11, 'Geriatrics'), (12, 'Gynaecology'), (13, 'Haematology'), (14, 'Hand Surgery'), (15, 'Infectious Disease'), (16, 'Internal Medicine'), (17, 'Oncology'), (18, 'Neonatology'), (19, 'Neurology'), (20, 'Obstetrics'), (21, 'Ophthalmology'), (22, 'Orthopaedic Surgery'), (23, 'Paediatric'), (24, 'Paediatric Surgery'), (25, 'Plastic Surgery'), (26, 'Psychiatry'), (27, 'Renal Medicine'), (28, 'Respiratory Medicine'), (29, 'Rheumatology'), (30, 'Urology')], default=1),
            preserve_default=True,
        ),
    ]
