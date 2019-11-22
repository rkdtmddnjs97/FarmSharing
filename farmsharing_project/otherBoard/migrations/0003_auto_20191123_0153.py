# Generated by Django 2.2.7 on 2019-11-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherBoard', '0002_auto_20191123_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='recruitment_number',
            new_name='joined_people',
        ),
        migrations.RemoveField(
            model_name='join',
            name='current_recruitment_condition',
        ),
        migrations.AddField(
            model_name='join',
            name='current_joined',
            field=models.BooleanField(default=True, max_length=200),
        ),
    ]
