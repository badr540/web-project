from django.shortcuts import render, redirect
import random as rand

scores = []    
scores.append(rand.randint(1000,5000))
for i in range(49):
    scores.append(rand.randint(max(scores[i-1] - 300, 0), scores[i-1] ))

def index(request):
    # this view return index
	return render(request, 'gamemodule/index.html')

def leaderboard(request):
    NumberOfElements = 10
    if request.method == "GET":
        if request.GET.get('Load') != None:
            NumberOfElements = int(request.GET.get('Load')) + int(request.GET.get('LoadSize')) 




    return render(request, 'gamemodule/leaderboard.html', {'scores': scores[0: min( NumberOfElements, len(scores)) ]})



def about(request):
    return render(request, 'gamemodule/about.html')