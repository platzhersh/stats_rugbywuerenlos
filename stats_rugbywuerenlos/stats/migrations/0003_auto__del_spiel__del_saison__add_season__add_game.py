# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting model 'Spiel'
        db.delete_table('stats_spiel')

        # Deleting model 'Saison'
        db.delete_table('stats_saison')

        # Adding model 'Season'
        db.create_table('stats_season', (
            ('start', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stats', ['Season'])

        # Adding model 'Game'
        db.create_table('stats_game', (
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Season'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pointsO', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opponent', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('stats', ['Game'])
    
    
    def backwards(self, orm):
        
        # Adding model 'Spiel'
        db.create_table('stats_spiel', (
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('saison', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.Saison'])),
            ('pointsO', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opponent', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('stats', ['Spiel'])

        # Adding model 'Saison'
        db.create_table('stats_saison', (
            ('start', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stats', ['Saison'])

        # Deleting model 'Season'
        db.delete_table('stats_season')

        # Deleting model 'Game'
        db.delete_table('stats_game')
    
    
    models = {
        'stats.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pointsO': ('django.db.models.fields.IntegerField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Season']"})
        },
        'stats.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['stats']
