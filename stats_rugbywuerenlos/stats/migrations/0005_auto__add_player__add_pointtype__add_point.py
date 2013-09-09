# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Player'
        db.create_table('stats_player', (
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('entry', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stats', ['Player'])

        # Adding model 'PointType'
        db.create_table('stats_pointtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('stats', ['PointType'])

        # Adding model 'Point'
        db.create_table('stats_point', (
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Player'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Game'])),
            ('pointType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.PointType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stats', ['Point'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Player'
        db.delete_table('stats_player')

        # Deleting model 'PointType'
        db.delete_table('stats_pointtype')

        # Deleting model 'Point'
        db.delete_table('stats_point')
    
    
    models = {
        'stats.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pointsO': ('django.db.models.fields.IntegerField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Season']"})
        },
        'stats.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'entry': ('django.db.models.fields.DateField', [], {}),
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
