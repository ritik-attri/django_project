from django.contrib import admin
from .models import Movie,Movie_Rating,Movie_CHARACTER,Movie_Directors
# Register your models here.
admin.site.register(Movie)
admin.site.register(Movie_Rating)
admin.site.register(Movie_CHARACTER)
admin.site.register(Movie_Directors)