# Generated by Django 3.1.6 on 2021-02-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='blogging', max_length=50),
        ),
    ]
