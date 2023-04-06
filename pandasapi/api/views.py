from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
import json
import pandas as pd

def getCsvFile(filenameinstorage):
    try:
        successful_file = staticfiles_storage.path(filenameinstorage)
        successful_file_df = pd.read_csv(successful_file)
        return successful_file_df
    except FileNotFoundError:
        print(f'File not found {filenameinstorage}')
        return None
    except Exception as e:
        print(f'Error reading file: {filenameinstorage}')
        return None

def index(request):
    return render(request, 'api/home.html')

# set api views here for each function
def get_future_job_trends(request , location):
    job_trend_file_name = 'database/job-trends.csv'
    results = []
    # Processing
    job_trends_df = getCsvFile(job_trend_file_name)
    if job_trends_df is not None:

        filt = job_trends_df['Location'].str.lower().str.strip().str.replace(" ", "") == location.lower().strip().replace(" ", "")
        columnsToGet = ['Ranking' , 'Future Job Predictions ']
        results = job_trends_df[filt][columnsToGet]
        results = results.to_json(orient='records')
        results = json.loads(results)
        if len(results) == 0:
            returnString = f"There is no '{location}' location available. Please make sure the name of the location right."
            return JsonResponse([{"error":returnString}] , safe=False)
        return JsonResponse(results , safe=False)
    else:
        return JsonResponse([{"error":"an error was encouncered during fetching of data."},] , safe=False)

def get_current_job_trends(request , location):
    results = []
    job_trend_file = 'database/job-trends.csv'
    # Processing
    job_trends_df = getCsvFile(job_trend_file)
    if job_trends_df is not None:

        filt = job_trends_df['Location'].str.lower().str.strip().str.replace(" ", "") == location.lower().strip().replace(" ", "")
        columnsToGet = ['Ranking' , 'Jobs Trending Now By Industry' , 'Job Description' , 'Profession Wage Per Area' , 'Living Wage Per Area']    
        results = job_trends_df[filt][columnsToGet]
        results = results.to_json(orient='records')
        results = json.loads(results)
        if len(results) == 0:
            returnString = f"There is no '{location}' location available. Please make sure the name of the location right."
            return JsonResponse([{"error":returnString}] , safe=False)
        return JsonResponse(results , safe=False)
    else:
        return JsonResponse([{"error":"an error was encouncered during fetching of data."},] , safe=False)


def get_available_programs(request , location):
    results = []
    available_programs_file = 'database/available_programs.csv'
    available_programs_df = getCsvFile(available_programs_file)

    if available_programs_df is not None:

        filt = available_programs_df['Location'].str.lower().str.strip().str.replace(" ", "") == location.lower().strip().replace(" ", "")
        columnsToGet = ['Available Program' , 'Description']
        results = available_programs_df[filt][columnsToGet]
        results = results.to_json(orient='records')
        results = json.loads(results)
        if len(results) == 0:
            returnString = f"There is no '{location}' location available. Please make sure the name of the location right."
            return JsonResponse([{"error":returnString}] , safe=False)
        return JsonResponse(results , safe=False)
    else:
        return JsonResponse([{"error":"an error was encouncered during fetching of data."},] , safe=False)

def get_trending_jobs(request , location):
    results = []
    job_searches_file = 'database/trending-job-searches-per-area.csv'
    job_searches_df = getCsvFile(job_searches_file)
    if job_searches_df is not None:

        filt = job_searches_df['Location'].str.lower().str.strip().str.replace(" ", "") == location.lower().strip().replace(" ", "")
        columnsToGet = ['Trending Job Searches ']
        results = job_searches_df[filt][columnsToGet]
        results = results.to_json(orient='records')
        results = json.loads(results)    
        if len(results) == 0:
            returnString = f"There is no '{location}' location available. Please make sure the name of the location right."
            return JsonResponse([{"error":returnString}] , safe=False)
        return JsonResponse(results , safe=False)
    else:
        return JsonResponse([{"error":"an error was encouncered during fetching of data."},] , safe=False)

def get_common_language(request , location):
    results = []
    location_file = 'database/location-information.csv'
    location_file_df = getCsvFile(location_file)
    if location_file_df is not None:
        filt = location_file_df['Location'].str.lower().str.strip().str.replace(" ", "") == location.lower().strip().replace(" ", "")
        columnsToGet = ['Language ']
        results = location_file_df[filt][columnsToGet]
        results = results.to_json(orient='records')
        results = json.loads(results)    
        if len(results) == 0:
            returnString = f"There is no '{location}' location available. Please make sure the name of the location right."
            return JsonResponse([{"error":returnString}] , safe=False)
        return JsonResponse(results , safe=False)
    else:
        return JsonResponse([{"error":"an error was encouncered during fetching of data."},] , safe=False)