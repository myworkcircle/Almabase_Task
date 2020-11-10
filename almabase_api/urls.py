
from django.contrib import admin
from django.urls import path,include
from .views import commitDetails
urlpatterns = [
    # endpoint for rest api
    path('commit/<str:organization>/<int:countOfRepos>/<int:countOfCommitees>/', commitDetails, name="number_of_commits")
]
