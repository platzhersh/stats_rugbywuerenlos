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
    ('^auth/login', 'stats_rugbywuerenlos.views.login'),
    ('^auth', 'stats_rugbywuerenlos.views.auth'),

)
