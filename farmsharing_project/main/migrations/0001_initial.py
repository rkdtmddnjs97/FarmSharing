
# Generated by Django 2.2.7 on 2019-11-29 12:02


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_owner', models.CharField(max_length=200, null=True)),
                ('land_user', models.CharField(max_length=200, null=True)),
                ('land', models.CharField(max_length=200, null=True)),
                ('request_condtion', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
