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
    results = []
    job_trend_file = staticfiles_storage.path('database/job-trends.csv')
    # Processing
    print(job_trend_file)
    job_trends_df = pd.read_csv(job_trend_file)
    filt = job_trends_df['Location'] == location
    columnsToGet = ['Ranking' , 'Jobs Trending Now By Industry' , 'Job Description' , 'Profession Wage Per Area' , 'Living Wage Per Area']    
    results = job_trends_df[filt][columnsToGet]
    results = results.to_json(orient='records')
    results = json.loads(results)
    return JsonResponse(results , safe=False)

def get_current_job_trends(request , location):

    return JsonResponse({})

def get_available_programs(request , location):

    return JsonResponse({})

def get_trending_jobs(request , location):

    return JsonResponse({})
