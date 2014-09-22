# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'ErrorInfo.hostname' to match new field type.
        db.rename_column(u'salt_MachineInfo_errorinfo', 'hostname', 'hostname_id')
        # Changing field 'ErrorInfo.hostname'
        db.alter_column(u'salt_MachineInfo_errorinfo', 'hostname_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salt_MachineInfo.BaseInfo']))
        # Adding index on 'ErrorInfo', fields ['hostname']
        db.create_index(u'salt_MachineInfo_errorinfo', ['hostname_id'])


        # Renaming column for 'InterfaceInfo.hostname' to match new field type.
        db.rename_column(u'salt_MachineInfo_interfaceinfo', 'hostname', 'hostname_id')
        # Changing field 'InterfaceInfo.hostname'
        db.alter_column(u'salt_MachineInfo_interfaceinfo', 'hostname_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salt_MachineInfo.BaseInfo']))
        # Adding index on 'InterfaceInfo', fields ['hostname']
        db.create_index(u'salt_MachineInfo_interfaceinfo', ['hostname_id'])


        # Renaming column for 'DiskInfo.hostname' to match new field type.
        db.rename_column(u'salt_MachineInfo_diskinfo', 'hostname', 'hostname_id')
        # Changing field 'DiskInfo.hostname'
        db.alter_column(u'salt_MachineInfo_diskinfo', 'hostname_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salt_MachineInfo.BaseInfo']))
        # Adding index on 'DiskInfo', fields ['hostname']
        db.create_index(u'salt_MachineInfo_diskinfo', ['hostname_id'])


    def backwards(self, orm):
        # Removing index on 'DiskInfo', fields ['hostname']
        db.delete_index(u'salt_MachineInfo_diskinfo', ['hostname_id'])

        # Removing index on 'InterfaceInfo', fields ['hostname']
        db.delete_index(u'salt_MachineInfo_interfaceinfo', ['hostname_id'])

        # Removing index on 'ErrorInfo', fields ['hostname']
        db.delete_index(u'salt_MachineInfo_errorinfo', ['hostname_id'])


        # Renaming column for 'ErrorInfo.hostname' to match new field type.
        db.rename_column(u'salt_MachineInfo_errorinfo', 'hostname_id', 'hostname')
        # Changing field 'ErrorInfo.hostname'
        db.alter_column(u'salt_MachineInfo_errorinfo', 'hostname', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Renaming column for 'InterfaceInfo.hostname' to match new field type.
        db.rename_column(u'salt_MachineInfo_interfaceinfo', 'hostname_id', 'hostname')
        # Changing field 'InterfaceInfo.hostname'
        db.alter_column(u'salt_MachineInfo_interfaceinfo', 'hostname', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Renaming column for 'DiskInfo.hostname' to match new field type.
        db.rename_column(u'salt_MachineInfo_diskinfo', 'hostname_id', 'hostname')
        # Changing field 'DiskInfo.hostname'
        db.alter_column(u'salt_MachineInfo_diskinfo', 'hostname', self.gf('django.db.models.fields.CharField')(max_length=60))

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
            'hostname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'disks'", 'to': u"orm['salt_MachineInfo.BaseInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mount': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'total': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'salt_MachineInfo.errorinfo': {
            'Meta': {'object_name': 'ErrorInfo'},
            'hostname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'errors'", 'to': u"orm['salt_MachineInfo.BaseInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'salt_MachineInfo.interfaceinfo': {
            'Meta': {'object_name': 'InterfaceInfo'},
            'hostname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interfaces'", 'to': u"orm['salt_MachineInfo.BaseInfo']"}),
            'hwaddr': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'ipaddr': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['salt_MachineInfo']