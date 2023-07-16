from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# This is a request handler
# request -> response
# request handler
# action (view)

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request): 
    x = calculate()
    return render(request, 'hello.html', {
        'name': 'wo'
    } )
    # return HttpResponse('Hello World!')