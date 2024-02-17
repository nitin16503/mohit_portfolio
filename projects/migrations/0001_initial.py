# Generated by Django 5.0.2 on 2024-02-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('project_name', models.CharField(max_length=80)),
                ('project_description', models.CharField(max_length=200)),
                ('project_Sills', models.CharField(max_length=200)),
                ('project_live_link', models.CharField(max_length=200)),
                ('project_github_link', models.CharField(max_length=200)),
                ('image_1', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(upload_to='images/')),
            ],
        ),
    ]