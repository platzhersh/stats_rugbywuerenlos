from django.conf import settings
from stats_rugbywuerenlos.stats.models import Player, Game, Point, PointType
from django.shortcuts import render_to_response
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import redirect

def listPlayers(request):
  p = Player.objects.all().order_by('firstName')
  return render_to_response('base_players.html', {'page_content':p}, context_instance=RequestContext(request))

def listPlayersDetail(request, playerID):
  p = Player.objects.get(id=playerID)
  return render_to_response('base_players_detail.html',{'player':p}, context_instance=RequestContext(request))


def listGames(request):
  g = Game.objects.all().order_by('date')
  return render_to_response('base_games.html', {'page_content':g},context_instance=RequestContext(request))

def listGamesDetail(request, gameID):
  g = Game.objects.get(id=gameID)
  p = Point.objects.filter(game=gameID)
  return render_to_response('base_games_detail.html',{'game':g,'points':p}, context_instance=RequestContext(request))

@login_required(login_url='/auth/login/')
def profile(request):
  return render_to_response('user/profile.html', {'request':request}, context_instance=RequestContext(request))

def logout_view(request):
  logout(request)
  return redirect('/auth/login/')
