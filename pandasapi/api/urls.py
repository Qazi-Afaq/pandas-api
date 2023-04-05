from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

app_name = 'homepage'

urlpatterns = [
    path("" , views.index , name='index'),
    # set get api paths here
    # get_current_job_trends
    path("api/get_future_job_trends/<location>" , views.get_future_job_trends , name='get_future_job_trends'),
    # get_future_job_trends
    path("api/get_current_job_trends/<location>" , views.get_current_job_trends , name='get_current_job_trends'),
    # get_available_programs
    path("api/get_available_programs/<location>" , views.get_available_programs , name='get_available_programs'),
    # get_trending_jobs
    path("api/get_trending_jobs/<location>" , views.get_trending_jobs , name='get_trending_jobs'),
    # get_common_language
]