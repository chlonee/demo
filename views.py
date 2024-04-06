from django.shortcuts import render
from .models import test_collection
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def job_matching_headhunt(request):
    return render(request, 'job_matching_headhunt.html')

def job_matching_candidate(request):
    return render(request, 'job_matching_candidate.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def index(request):
    return HttpResponse("<h1> App is running </h1>")

def add_data(request):
    records = {
        'first_name': "John",
        'last_name': 'Doe'
    }
    test_collection.insert_one(records)
    return HttpResponse('<h1> New record is added </h1>')

def get_all_data(request):
    record = test_collection.find()
    return HttpResponse(record)
