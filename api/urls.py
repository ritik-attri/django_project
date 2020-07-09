from django.contrib import admin
from django.urls import path
from .views import MovieViewSet,loggin_inViewSet#,MovieCharactersViewSet,MovieDirectorsViewSet,MovieRatingViewSet
from rest_framework import routers
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token
router=routers.DefaultRouter()
router.register('',MovieViewSet)
#router.register('characters/',MovieCharactersViewSet,basename='characters')
#router.register('directors/',MovieDirectorsViewSet,basename='directors')
#router.register('ratings/',MovieRatingViewSet,basename='ratings')
login_router=routers.DefaultRouter()
login_router.register('',loggin_inViewSet)
urlpatterns = [
    path('login/',include(login_router.urls)),
    path('movies/', include(router.urls)),
    path('auth/',obtain_auth_token),
]
