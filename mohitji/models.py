from django.db import models


# Create your models here.

class Projects(models.Model):

    project_id = models.AutoField(primary_key=True,unique=True)
    project_name = models.CharField(max_length=80)
    project_description = models.CharField(max_length=200)
    project_Sills = models.CharField(max_length=200)
    project_live_link = models.CharField(max_length=200)
    project_github_link = models.CharField(max_length=200)
    image_1 = models.ImageField(upload_to='images/')  # Define the image field
    image_2 = models.ImageField(upload_to='images/')  # Define the image field

    

    def __str__(self):
        return self.project_name
    

    









