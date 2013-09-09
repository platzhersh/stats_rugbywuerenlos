from stats_rugbywuerenlos.stats.models import Season, Game, PointType, Point, Player
from django.contrib import admin

class SeasonAdmin(admin.ModelAdmin):
    fields = ['start']

admin.site.register(Season, SeasonAdmin)

class PointInline(admin.TabularInline):
    model = Point
    extra = 3

class GameAdmin(admin.ModelAdmin):
    inlines = [PointInline]
    list_filter = ['season']
    search_fields = ['opponent','location']
    list_display = ('opponent','season','date','location','get_points','pointsO')
 
admin.site.register(Game, GameAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('get_name','entry','birthdate','get_points')
    search_fields = ['get_name']

admin.site.register(PointType)
admin.site.register(Player, PlayerAdmin)
