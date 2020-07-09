from django.db import models
import uuid
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Movie(models.Model):
    Movie_Name=models.CharField(max_length=35,blank=False,unique=True)
    Movie_Description=models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.Movie_Name
class Movie_CHARACTER(models.Model):
    Movie_Character=models.CharField(max_length=20,blank=True)
    Movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='Movie_CHARACTER',blank=True)
    def __str__(self):
        return self.Movie_Character
class Movie_Directors(models.Model):
    Movie_Director=models.CharField(max_length=35,blank=True)
    Movie=models.ManyToManyField(Movie,related_name='Movie_Director',blank=True)

    def __str__(self):
        return self.Movie_Director
class Movie_Rating(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='Movie_Ratings')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Movie_Ratings = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],blank=False,null=True)
    class Meta:
        unique_together=(('user','movie'))
        index_together=(('user','movie'))
    def __str__(self):
        return str(self.Movie_Ratings)

