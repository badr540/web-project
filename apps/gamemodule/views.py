from django.shortcuts import render, redirect

def index(request):
    # this view return index
	return render(request, 'gamemodule/index.html')

def leaderboard(request):
    return render(request, 'gamemodule/leaderboard.html')

def about(request):
    return render(request, 'gamemodule/about.html')