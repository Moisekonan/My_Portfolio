# Generated by Django 4.2.2 on 2023-06-21 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_blog_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
