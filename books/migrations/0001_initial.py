# Generated by Django 3.0.6 on 2020-05-15 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=40)),
                ('book_name', models.CharField(max_length=200)),
                ('pub_year', models.IntegerField()),
            ],
        ),
    ]
