# Generated by Django 3.2.2 on 2021-05-08 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210508_0910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
