from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello World!")
# Create your views here.

def About_me(request):
	return render(request, 'main.html')
