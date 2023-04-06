from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
import json
import pandas as pd



def index(request):
    return HttpResponse("Welcome, Please use the following commands to fetch information:")

# set api views here for each function
def get_future_job_trends(request , location):
    job_trend_file = staticfiles_storage.path('database/job-trends.csv')

    results = []
    
    # Processing
    job_trends_df = pd.read_csv(job_trend_file)
    filt = job_trends_df['Location'] == location
    columnsToGet = ['Ranking' , 'Future Job Predictions ']
    results = job_trends_df[filt][columnsToGet]
    results = results.to_json(orient='records')
    results = json.loads(results)
    return JsonResponse(results , safe=False)

def get_current_job_trends(request , location):
    results = []
    job_trend_file = staticfiles_storage.path('database/job-trends.csv')
    # Processing
    job_trends_df = pd.read_csv(job_trend_file)
    filt = job_trends_df['Location'] == location
    columnsToGet = ['Ranking' , 'Jobs Trending Now By Industry' , 'Job Description' , 'Profession Wage Per Area' , 'Living Wage Per Area']    
    results = job_trends_df[filt][columnsToGet]
    results = results.to_json(orient='records')
    results = json.loads(results)
    
    return JsonResponse(results , safe=False)

def get_available_programs(request , location):
    results = []
    available_programs_file = staticfiles_storage.path('database/available_programs.csv')
    available_programs_df = pd.read_csv(available_programs_file)
    filt = available_programs_df['Location'] == location
    columnsToGet = ['Available Program' , 'Description']
    results = available_programs_df[filt][columnsToGet]
    results = results.to_json(orient='records')
    results = json.loads(results)

    return JsonResponse(results , safe=False)

def get_trending_jobs(request , location):
    results = []
    job_searches_file = staticfiles_storage.path('database/trending-job-searches-per-area.csv')
    df = pd.read_csv(job_searches_file)
    filt = df['Location'] == location
    columnsToGet = ['Trending Job Searches ']
    results = df[filt][columnsToGet]
    results = results.to_json(orient='records')
    results = json.loads(results)    
    
    return JsonResponse(results , safe=False)

def get_common_language(request , location):
    results = []
    job_searches_file = staticfiles_storage.path('database/location-information.csv')
    df = pd.read_csv(job_searches_file)
    filt = df['Location'] == location
    columnsToGet = ['Language ']
    results = df[filt][columnsToGet]
    results = results.to_json(orient='records')
    results = json.loads(results)    
    
    return JsonResponse(results , safe=False)
