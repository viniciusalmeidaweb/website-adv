# Generated by Django 5.1.7 on 2025-06-30 14:51

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_post_photo_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='Nome da categoria da noticia', unique=True),
        ),
    ]
