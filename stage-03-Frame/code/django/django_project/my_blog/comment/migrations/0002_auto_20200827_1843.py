# Generated by Django 2.2 on 2020-08-27 10:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]