# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Spiel'
        db.create_table('stats_spiel', (
            ('saison', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Saison'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pointsO', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opponent', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('stats', ['Spiel'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Spiel'
        db.delete_table('stats_spiel')
    
    
    models = {
        'stats.saison': {
            'Meta': {'object_name': 'Saison'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'stats.spiel': {
            'Meta': {'object_name': 'Spiel'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pointsO': ('django.db.models.fields.IntegerField', [], {}),
            'saison': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Saison']"})
        }
    }
    
    complete_apps = ['stats']
