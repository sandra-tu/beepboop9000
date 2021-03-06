# Generated by Django 3.2.8 on 2021-10-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.CharField(choices=[('gb', 'Great Britain'), ('ie', 'Ireland')], max_length=50)),
                ('city', models.CharField(choices=[('edi', 'Edinburgh')], max_length=50)),
                ('type', models.CharField(choices=[('pubbar', 'Pub/Bar'), ('club', 'Nightclub'), ('soc', 'University Society'), ('school', 'School'), ('office', 'Office'), ('store', 'Store'), ('other', 'Other')], max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('report_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
