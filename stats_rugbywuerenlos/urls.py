from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),
    (r'^$', TemplateView.as_view(template_name='base.html')),
    ('^admin/', include(admin.site.urls)),

    ('^players/(?P<playerID>\d+)','stats_rugbywuerenlos.views.listPlayersDetail'),
    ('^players', 'stats_rugbywuerenlos.views.listPlayers'),

    ('^games/(?P<gameID>\d+)','stats_rugbywuerenlos.views.listGamesDetail'),
    ('^games', 'stats_rugbywuerenlos.views.listGames'),
    ('^auth/profile/$', 'stats_rugbywuerenlos.views.profile'),
    ('^auth/login/', 'django.contrib.auth.views.login', {'template_name':'base_login.html'}),
    ('^auth/logout/', 'stats_rugbywuerenlos.views.logout_view'),
#    ('^auth', 'stats_rugbywuerenlos.views.auth'),

    ('^REST/players/(?P<playerID>\d+)', 'stats_rugbywuerenlos.views.playersDetailJSON'),
    ('^REST/players', 'stats_rugbywuerenlos.views.playersJSON'),
    ('^REST/games', 'stats_rugbywuerenlos.views.gamesJSON'),
    ('^REST/seasons', 'stats_rugbywuerenlos.views.seasonsJSON'),

)
