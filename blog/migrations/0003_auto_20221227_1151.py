# Generated by Django 3.1.6 on 2022-12-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(),
        ),
    ]