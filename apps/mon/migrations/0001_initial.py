# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Record'
        db.create_table('mon_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('current', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('volt', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('temp', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('light', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('mon', ['Record'])


    def backwards(self, orm):
        
        # Deleting model 'Record'
        db.delete_table('mon_record')


    models = {
        'mon.record': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Record'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'light': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'volt': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'})
        }
    }

    complete_apps = ['mon']
