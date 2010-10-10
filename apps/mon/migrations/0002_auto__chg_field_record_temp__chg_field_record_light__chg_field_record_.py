# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Record.temp'
        db.alter_column('mon_record', 'temp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

        # Changing field 'Record.light'
        db.alter_column('mon_record', 'light', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

        # Changing field 'Record.current'
        db.alter_column('mon_record', 'current', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2))

        # Changing field 'Record.volt'
        db.alter_column('mon_record', 'volt', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3))


    def backwards(self, orm):
        
        # Changing field 'Record.temp'
        db.alter_column('mon_record', 'temp', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'Record.light'
        db.alter_column('mon_record', 'light', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'Record.current'
        db.alter_column('mon_record', 'current', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2))

        # Changing field 'Record.volt'
        db.alter_column('mon_record', 'volt', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3))


    models = {
        'mon.record': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Record'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'light': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'temp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'volt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3'})
        }
    }

    complete_apps = ['mon']
