# Generated by Django 3.2.2 on 2021-05-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_comment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='* * *', verbose_name='текст'),
        ),
    ]
