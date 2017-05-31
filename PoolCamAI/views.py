from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'PoolCamAI/index.html')


def main(request):
    return render(request, 'PoolCamAI/main.html')

