# Generated by Django 3.1.6 on 2021-02-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='airtable_id',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
