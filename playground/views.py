from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# This is a request handler
# request -> response
# request handler
# action (view)

def say_hello(request): 
    return render(request, 'hello.html', {
        'name': 'World'
    } )
    # return HttpResponse('Hello World!')