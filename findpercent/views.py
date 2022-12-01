from django.shortcuts import render
from django.http import HttpResponse
import miss


# Create your views here.
def index(request):
    return HttpResponse(miss.miss())
