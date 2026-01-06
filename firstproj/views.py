from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits


def home_view(request, *args, **kwargs):
    mycontext = {
        "Name" : 'Tufail'
    }
    return render(request, "home.html", mycontext)