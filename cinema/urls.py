from django.urls import path
from cinema.views import *

app_name = "cinema"

urlpatterns = [
    path("movie/", movie_list, name="movie_list"),
    path("movie/<int:pk>/", movie_detail, name="movie_detail"),
]
