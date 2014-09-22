# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ErrorInfo.info'
        db.alter_column(u'salt_MachineInfo_errorinfo', 'info', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'ErrorInfo.info'
        db.alter_column(u'salt_MachineInfo_errorinfo', 'info', self.gf('django.db.models.fields.CharField')(max_length=60))

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
        },
        u'salt_MachineInfo.diskinfo': {
            'Meta': {'object_name': 'DiskInfo'},
            'available': ('django.db.models.fields.BigIntegerField', [], {}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mount': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'total': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'salt_MachineInfo.errorinfo': {
            'Meta': {'object_name': 'ErrorInfo'},
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'salt_MachineInfo.interfaceinfo': {
            'Meta': {'object_name': 'InterfaceInfo'},
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'hwaddr': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'ipaddr': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['salt_MachineInfo']