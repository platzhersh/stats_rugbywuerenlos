# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Game.tom'
        db.add_column('stats_game', 'tom', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tom', null=True, to=orm['stats.Player']), keep_default=False)

        # Adding field 'Game.mom'
        db.add_column('stats_game', 'mom', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mom', null=True, to=orm['stats.Player']), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Game.tom'
        db.delete_column('stats_game', 'tom_id')

        # Deleting field 'Game.mom'
        db.delete_column('stats_game', 'mom_id')
    
    
    models = {
        'stats.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mom'", 'null': 'True', 'to': "orm['stats.Player']"}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pointsO': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Season']"}),
            'tom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tom'", 'null': 'True', 'to': "orm['stats.Player']"})
        },
        'stats.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        'stats.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['stats']
