# Generated by Django 5.0.2 on 2024-02-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_image_1_alter_projects_image_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image_1',
            field=models.ImageField(upload_to='static/project_images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image_2',
            field=models.ImageField(upload_to='static/project_images/'),
        ),
    ]