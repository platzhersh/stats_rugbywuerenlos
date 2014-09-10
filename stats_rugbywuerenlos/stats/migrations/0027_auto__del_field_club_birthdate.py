# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Club.birthdate'
        db.delete_column(u'stats_club', 'birthdate')


    def backwards(self, orm):
        # Adding field 'Club.birthdate'
        db.add_column(u'stats_club', 'birthdate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'stats.association': {
            'Meta': {'object_name': 'Association'},
            'fullName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortName': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
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
        u'stats.club': {
            'Meta': {'object_name': 'Club'},
            'association': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Association']", 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pitch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Location']", 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '599', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
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
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Club']", 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pitch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.Location']", 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']