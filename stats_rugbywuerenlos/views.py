from django.conf import settings
from stats_rugbywuerenlos.stats.models import Player, Game, Point, PointType
from django.shortcuts import render_to_response
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def listPlayers(request):
  p = Player.objects.all().order_by('firstName')
  return render_to_response('base_players.html', {'page_content':p})

def listPlayersDetail(request, playerID):
  p = Player.objects.get(id=playerID)
  return render_to_response('base_players_detail.html',{'player':p})


def listGames(request):
  g = Game.objects.all().order_by('date')
  return render_to_response('base_games.html', {'page_content':g})

def listGamesDetail(request, gameID):
  g = Game.objects.get(id=gameID)
  p = Point.objects.filter(game=gameID)
  return render_to_response('base_games_detail.html',{'game':g,'points':p})

@login_required(login_url='/auth/login/')
def auth(request):
  html = "<html><body>You are in!</body></html>"
  return HttpResponse(html)

def login(request):
  html=  "<html><body>Login</body></html>"
  return HttpResponse(html)
