from django.shortcuts import render
import time
from django.http import HttpResponse

def slow_view(request):
    time.sleep(4)
    return HttpResponse("teste de view lenta")
