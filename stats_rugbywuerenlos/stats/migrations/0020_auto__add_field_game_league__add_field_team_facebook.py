# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.league'
        db.add_column(u'stats_game', 'league',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['stats.League']),
                      keep_default=False)

        # Adding field 'Team.facebook'
        db.add_column(u'stats_team', 'facebook',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.league'
        db.delete_column(u'stats_game', 'league_id')

        # Deleting field 'Team.facebook'
        db.delete_column(u'stats_team', 'facebook')


    models = {
        u'stats.card': {
            'Meta': {'object_name': 'Card'},
            'cardType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.CardType']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Player']"})
        },
        u'stats.cardtype': {
            'Meta': {'object_name': 'CardType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stats.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'guestteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guestteam_set'", 'to': u"orm['stats.Team']"}),
            'homegame': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hostteam_set'", 'to': u"orm['stats.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.League']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mom'", 'null': 'True', 'to': u"orm['stats.Player']"}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pointsO': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Season']"}),
            'tom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tom'", 'null': 'True', 'to': u"orm['stats.Player']"})
        },
        u'stats.league': {
            'Meta': {'object_name': 'League'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stats.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'})
        },
        u'stats.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        u'stats.point': {
            'Meta': {'object_name': 'Point'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Player']"}),
            'pointType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.PointType']"})
        },
        u'stats.pointtype': {
            'Meta': {'object_name': 'PointType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'stats.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stats.season': {
            'Meta': {'object_name': 'Season'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        u'stats.team': {
            'Meta': {'object_name': 'Team'},
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pitch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Location']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['stats']