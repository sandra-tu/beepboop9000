# Generated by Django 3.2.3 on 2021-10-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20211017_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='city',
            field=models.CharField(choices=[('edinburgh', 'Edinburgh'), ('dublin', 'Dublin')], max_length=50),
        ),
    ]
