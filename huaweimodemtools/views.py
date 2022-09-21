from django.shortcuts import render
from random import seed
from random import randint
from django.http import HttpResponse
# Create your views here.

seed(1)

def generate_random(request):
	return render(request, "form.html")

def generate_number(request):
	return HttpResponse(randint(0, 30));