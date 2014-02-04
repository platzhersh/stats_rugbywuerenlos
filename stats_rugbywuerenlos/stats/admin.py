from stats_rugbywuerenlos.stats.models import Season, Game, PointType, Point, Player, League, Location, Team, CardType, Card, Position
from django.contrib import admin

class SeasonAdmin(admin.ModelAdmin):
    fields = ['start']

admin.site.register(Season, SeasonAdmin)

class PointInline(admin.TabularInline):
    model = Point
    extra = 3

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

class GameAdmin(admin.ModelAdmin):
    inlines = [PointInline,CardInline]
    list_filter = ['season','hostteam','guestteam','location']
    search_fields = ['hostteam','guestteam','location']
    list_display = ('__unicode__','hostteam','guestteam','season','date','location','get_points','pointsO')
 
admin.site.register(Game, GameAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('get_name','position','entry','birthdate','points')
    search_fields = ['get_name']

admin.site.register(Position)
admin.site.register(Card)
admin.site.register(Point)
admin.site.register(PointType)
admin.site.register(CardType)
admin.site.register(League)
admin.site.register(Location)
admin.site.register(Team)
admin.site.register(Player, PlayerAdmin)
