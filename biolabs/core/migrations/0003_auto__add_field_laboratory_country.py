# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Laboratory.country'
        db.add_column(u'core_laboratory', 'country',
                      self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Laboratory.country'
        db.delete_column(u'core_laboratory', 'country')


    models = {
        u'core.laboratory': {
            'Meta': {'object_name': 'Laboratory'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['core']