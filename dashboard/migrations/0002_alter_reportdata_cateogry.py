# Generated by Django 4.0 on 2021-12-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdata',
            name='cateogry',
            field=models.CharField(choices=[('PL', 'Plumbing'), ('EL', 'Electrical'), ('MT', 'Maintenance'), ('CAS', 'CUSTODIAL')], max_length=50),
        ),
    ]
