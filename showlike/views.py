from django.shortcuts import render
from django.views import generic

def home(request):
	context = {'test': 'test'}
	return render(request, 'index.html', context)