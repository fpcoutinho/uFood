from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def homepage(request):
    return render(request, settings.BASE_DIR/'templates/base.html')