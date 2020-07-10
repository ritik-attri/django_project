from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Movie,Movie_Rating,Movie_Directors,Movie_CHARACTER
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.decorators import action
from .serializers import MovieSerializer,UserSerializer #,MovieRatingSerializer,MovieCharacterSerializer,MovieDirectorSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.views import View
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    @action(detail=False,methods=['GET'])
    def view_movie(self,request,pk=None):
       print(request.data['Movie_Name'])
       if 'Movie_Name' in request.data:
           try:
               movie=Movie.objects.get(request.data['Movie_Name'])
               response={'message':'This movie has already been created, you can add ratings,characters and directors by logging in.For that, go to http://localhost/api/login'}






           except:
               Movie.objects.create(Movie_Name=request.data['Movie_Name'])
               response = {'movie_created':movie.objects.all()}

           return Response(response,status=status.HTTP_200_OK)
       else:
           response={'message':'move not created'}
           return Response(response,status=status.HTTP_400_BAD_REQUEST)


class loggin_inViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #authentication_classes = [TokenAuthentication,]
    queryset = User.objects.all()
    @action(detail=True,methods=['GET'])
    def redirecting_request(self,request):
        return redirect('http://localhost/api/movies/',permanent=True)















































'''class MovieRatingViewSet(viewsets.ModelViewSet):
    queryset = Movie_Rating.objects.all()
    serializer_class = MovieRatingSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    @action(detail=False, methods=['GET'])
    def rate_movie(self, request, pk=None):
        if 'Rating' in request.data:
            response = {'message': 'Done!'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Not Done!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MovieCharactersViewSet(viewsets.ModelViewSet):
    queryset = Movie_CHARACTER.objects.all()
    serializer_class = MovieCharacterSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

class MovieDirectorsViewSet(viewsets.ModelViewSet):
    queryset = Movie_Directors.objects.all()
    serializer_class = MovieDirectorSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)'''


