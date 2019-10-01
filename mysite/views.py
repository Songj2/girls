from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('여기는 송지현의 홈페이지')