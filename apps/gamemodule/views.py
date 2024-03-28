from django.shortcuts import render, redirect
import random as rand
from .models import HighScores

def index(request):
    # this view return index
	return render(request, 'gamemodule/index.html')

def leaderboard(request):
    NumberOfElements = 10
    if request.method == "GET":
        if request.GET.get('Load') != None:
            NumberOfElements = int(request.GET.get('Load')) + int(request.GET.get('LoadSize')) 
            


    highScores = list(HighScores.objects.values_list('score', flat=True))


    return render(request, 'gamemodule/leaderboard.html', {'scores': highScores[0:NumberOfElements]})



def about(request):
    return render(request, 'gamemodule/about.html')