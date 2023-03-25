from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
# Create your views here.
def index(request):
    return HttpResponse("Hello World welcome to my tournament page")
def details(request):
    players =Player.objects.all()
    players = [
        f"{player.firstname} {player.lastname} " for player in players
    ]
    return HttpResponse(players)