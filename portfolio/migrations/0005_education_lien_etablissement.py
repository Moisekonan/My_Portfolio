# Generated by Django 4.2.2 on 2023-06-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_categorie_remove_project_category_project_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='lien_etablissement',
            field=models.URLField(blank=True, null=True),
        ),
    ]
