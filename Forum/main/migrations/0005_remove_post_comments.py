# Generated by Django 4.0.1 on 2022-01-22 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_reply_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
