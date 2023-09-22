# Generated by Django 4.2.5 on 2023-09-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='social_link',
            field=models.URLField(blank=True, help_text='Artist Profile', max_length=50, unique=True),
        ),
    ]
