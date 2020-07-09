from rest_framework import serializers
from .models import Movie_CHARACTER,Movie_Directors,Movie_Rating,Movie
from django.contrib.auth.hashers import make_password
import ast
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')
        def create(self,validated_data):
            User.objects.create(username=validated_data['username'],password=make_password(['password']))

class MovieCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie_CHARACTER
        fields=('Movie','Movie_Character')

class MovieDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie_Directors
        fields=('Movie','Movie_Directors',)

class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie_Rating
        fields=('movie','user','Movie_Ratings')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('Movie_Name','Movie_Description')


