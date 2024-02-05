from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

challenges  ={
    'january':'Eat no meat for the entire month',
    'february':'Walk for at least 20 minutes every day',
    'march':'Learn Django for at least 20 minutes every day',
    'april':'Learn Django for at least 20 minutes every day',
    'may':'Learn Django for at least 20 minutes every day',
    'june':'Learn Django for at least 20 minutes every day',
    'july':'Learn Django for at least 20 minutes every day',
    'august':'Learn Django for at least 20 minutes every day',
    'september':'Learn Django for at least 20 minutes every day',
    'october':'Learn Django for at least 20 minutes every day',
    'november':'Learn Django for at least 20 minutes every day',
    'december':'Learn Django for at least 20 minutes every day'

}


# Create your views here.
def index(request):
    return HttpResponse("My first website")


def monthly_challenges(request, month):
    try:

        return HttpResponse(f"{month} challenges")
    except:
        print("Value n")

