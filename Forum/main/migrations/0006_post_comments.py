# Generated by Django 4.0.1 on 2022-01-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='main.Comment'),
        ),
    ]
