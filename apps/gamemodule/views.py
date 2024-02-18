from django.shortcuts import render, redirect

def index(request):
    # this view return index
	return render(request, 'gamemodule/index.html')
