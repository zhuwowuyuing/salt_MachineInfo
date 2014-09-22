# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InterfaceInfo'
        db.create_table(u'salt_MachineInfo_interfaceinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('interface', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('hwaddr', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('ipaddr', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'salt_MachineInfo', ['InterfaceInfo'])

        # Adding model 'DiskInfo'
        db.create_table(u'salt_MachineInfo_diskinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('mount', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('available', self.gf('django.db.models.fields.IntegerField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'salt_MachineInfo', ['DiskInfo'])


    def backwards(self, orm):
        # Deleting model 'InterfaceInfo'
        db.delete_table(u'salt_MachineInfo_interfaceinfo')

        # Deleting model 'DiskInfo'
        db.delete_table(u'salt_MachineInfo_diskinfo')


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
            'available': ('django.db.models.fields.IntegerField', [], {}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mount': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'total': ('django.db.models.fields.IntegerField', [], {})
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