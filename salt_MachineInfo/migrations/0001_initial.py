# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseInfo'
        db.create_table(u'salt_MachineInfo_baseinfo', (
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=60, primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cpu_model', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('num_cpus', self.gf('django.db.models.fields.IntegerField')()),
            ('mem_total', self.gf('django.db.models.fields.IntegerField')()),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('productname', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'salt_MachineInfo', ['BaseInfo'])


    def backwards(self, orm):
        # Deleting model 'BaseInfo'
        db.delete_table(u'salt_MachineInfo_baseinfo')


    models = {
        u'salt_MachineInfo.baseinfo': {
            'Meta': {'object_name': 'BaseInfo'},
            'cpu_model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'mem_total': ('django.db.models.fields.IntegerField', [], {}),
            'num_cpus': ('django.db.models.fields.IntegerField', [], {}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'productname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['salt_MachineInfo']