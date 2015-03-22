# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Laboratory.description'
        db.alter_column(u'core_laboratory', 'description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

        # Changing field 'Laboratory.longitude'
        db.alter_column(u'core_laboratory', 'longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=8))

        # Changing field 'Laboratory.latitude'
        db.alter_column(u'core_laboratory', 'latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8))

        # Changing field 'Laboratory.adress'
        db.alter_column(u'core_laboratory', 'adress', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

    def backwards(self, orm):

        # Changing field 'Laboratory.description'
        db.alter_column(u'core_laboratory', 'description', self.gf('django.db.models.fields.CharField')(default='description', max_length=300))

        # Changing field 'Laboratory.longitude'
        db.alter_column(u'core_laboratory', 'longitude', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=8))

        # Changing field 'Laboratory.latitude'
        db.alter_column(u'core_laboratory', 'latitude', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=8))

        # Changing field 'Laboratory.adress'
        db.alter_column(u'core_laboratory', 'adress', self.gf('django.db.models.fields.CharField')(default='address', max_length=300))

    models = {
        u'core.laboratory': {
            'Meta': {'object_name': 'Laboratory'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
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