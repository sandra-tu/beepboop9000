# Generated by Django 3.2.8 on 2021-10-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='organisation',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='city',
            field=models.CharField(choices=[('edi', 'Edinburgh')], max_length=50),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='country',
            field=models.CharField(choices=[('gb', 'Great Britain'), ('ie', 'Ireland')], max_length=50),
        ),
    ]