# Generated by Django 3.0.1 on 2020-01-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherprofile', '0003_auto_20200122_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='course',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
