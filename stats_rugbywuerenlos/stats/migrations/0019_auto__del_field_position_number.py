# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'Position.number'
        db.delete_column('stats_position', 'number')
    
    
    def backwards(self, orm):
        
        # Adding field 'Position.number'
        db.add_column('stats_position', 'number', self.gf('django.db.models.fields.IntegerField')(default=''), keep_default=False)
    
    
    models = {
        'stats.card': {
            'Meta': {'object_name': 'Card'},
            'cardType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.CardType']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Player']"})
        },
        'stats.cardtype': {
            'Meta': {'object_name': 'CardType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stats.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'guestteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guestteam_set'", 'to': "orm['stats.Team']"}),
            'homegame': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'hostteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hostteam_set'", 'to': "orm['stats.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mom'", 'null': 'True', 'to': "orm['stats.Player']"}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pointsO': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Season']"}),
            'tom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tom'", 'null': 'True', 'to': "orm['stats.Player']"})
        },
        'stats.league': {
            'Meta': {'object_name': 'League'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stats.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'})
        },
        'stats.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        'stats.point': {
            'Meta': {'object_name': 'Point'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Player']"}),
            'pointType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.PointType']"})
        },
        'stats.pointtype': {
            'Meta': {'object_name': 'PointType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'stats.position': {
            'Meta': {'object_name': 'Position'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stats.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'stats.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pitch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Location']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        }
    }
    
    complete_apps = ['stats']
