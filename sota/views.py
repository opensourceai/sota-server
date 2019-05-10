from django.shortcuts import render
from django.http import HttpResponse
from .sotawhat import sota
import json


# Create your views here.


def index(request):
    try:
        keyword = request.GET.get("keyword")
        num_results = int(request.GET.get("num_results"))
        print(keyword, num_results)
    except:
        keyword = 'ml'
        num_results = 5
    results = sota(keyword, num_results)
    print(request)
    return HttpResponse(json.dumps(results), content_type="application/json")
