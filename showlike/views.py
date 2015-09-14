from django.shortcuts import render
from django.views import generic

import urllib
import urllib2
import json

def home(request):
	context = {'test': 'test'}
	return render(request, 'index.html', context)

def search(request):
	query = request.GET['query']
	query = urllib.unquote(query.encode('ascii')).decode('utf-8')
	query = urllib.quote(query.encode('utf-8'))
	stuff = urllib2.urlopen('http://www.tastekid.com/api/similar?q='+query+'&k=159747-ShowLike-M27GAIEQ&verbose=1')
	decoded = json.load(stuff)
	context = {	
				'keywords': request.GET['query'],
				'info' : decoded['Similar']['Info'],
				'results': decoded['Similar']['Results']	
			}

	return render(request, 'search.html', context)