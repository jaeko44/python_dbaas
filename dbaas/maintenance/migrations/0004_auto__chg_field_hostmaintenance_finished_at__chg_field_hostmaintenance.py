# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HostMaintenance.finished_at'
        db.alter_column(u'maintenance_hostmaintenance', 'finished_at', self.gf(
            'django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'HostMaintenance.started_at'
        db.alter_column(u'maintenance_hostmaintenance', 'started_at', self.gf(
            'django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'HostMaintenance.main_log'
        db.alter_column(u'maintenance_hostmaintenance', 'main_log', self.gf(
            'django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'HostMaintenance.finished_at'
        db.alter_column(u'maintenance_hostmaintenance', 'finished_at', self.gf(
            'django.db.models.fields.DateTimeField')(default=None))

        # Changing field 'HostMaintenance.started_at'
        db.alter_column(u'maintenance_hostmaintenance', 'started_at', self.gf(
            'django.db.models.fields.DateTimeField')(default=None))

        # Changing field 'HostMaintenance.main_log'
        db.alter_column(u'maintenance_hostmaintenance', 'main_log', self.gf(
            'django.db.models.fields.TextField')(default=None))

    models = {
        u'maintenance.hostmaintenance': {
            'Meta': {'object_name': 'HostMaintenance'},
            'check_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'host_maintenance'", 'to': u"orm['physical.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'maintenance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'maintenance'", 'to': u"orm['maintenance.Maintenance']"}),
            'rollback_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'maintenance.maintenance': {
            'Meta': {'object_name': 'Maintenance'},
            'check_script': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'host_query': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_script': ('django.db.models.fields.TextField', [], {}),
            'maximum_workers': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'rollback_script': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'scheduled_for': ('django.db.models.fields.DateTimeField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'physical.host': {
            'Meta': {'object_name': 'Host'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitor_url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maintenance']
