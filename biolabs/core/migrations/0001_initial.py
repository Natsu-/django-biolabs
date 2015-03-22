# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Laboratory'
        db.create_table(u'core_laboratory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('is_moderated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=8)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=8)),
        ))
        db.send_create_signal(u'core', ['Laboratory'])


    def backwards(self, orm):
        # Deleting model 'Laboratory'
        db.delete_table(u'core_laboratory')


    models = {
        u'core.laboratory': {
            'Meta': {'object_name': 'Laboratory'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '8'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['core']