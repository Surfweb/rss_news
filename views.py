from django.http import HttpResponse
from django.shortcuts import render

from rss_news.models import Post

import random


# Create your views here.

def index(request):
	#return HttpResponse("Hi")
	
	number = random.randrange(0,100)
    
	context = { 	# Dictionary
		'value': 'Hello Python',
		'number': str(number),
	}
	return render(request, "index.html", context)