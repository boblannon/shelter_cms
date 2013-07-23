# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LongtermStatus'
        db.create_table('directory_longtermstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('permanent', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
        ))
        db.send_create_signal('directory', ['LongtermStatus'])

        # Adding model 'CurrentStatus'
        db.create_table('directory_currentstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('directory', ['CurrentStatus'])

        # Adding model 'Tag'
        db.create_table('directory_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('directory', ['Tag'])

        # Adding model 'Contact'
        db.create_table('directory_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('directory', ['Contact'])

        # Adding model 'Location'
        db.create_table('directory_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street_one', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('street_two', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('directory', ['Location'])

        # Adding model 'Resource'
        db.create_table('directory_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('homepage', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('longterm_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.LongtermStatus'], null=True, on_delete=models.PROTECT, blank=True)),
            ('locations', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'], null=True, blank=True)),
            ('contacts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Contact'], null=True, blank=True)),
            ('transitional_housing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('affordable_housing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('drop_in', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('men', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('women', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mother_and_child', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('father_and_child', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('under_18', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('family', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('showers', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clothing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('transportation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('telephones', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('education_training', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('drug_rehab', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('food', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('case_management', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('health_center', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('laundry', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mental_health', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dental', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('job_attire', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('job_training', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('career_center', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bike_repair', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('social_services', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wheelchair_repair', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail_pickup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('computer_center', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('directory', ['Resource'])

        # Adding M2M table for field tags on 'Resource'
        db.create_table('directory_resource_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm['directory.resource'], null=False)),
            ('tag', models.ForeignKey(orm['directory.tag'], null=False))
        ))
        db.create_unique('directory_resource_tags', ['resource_id', 'tag_id'])

        # Adding model 'StatusUpdate'
        db.create_table('directory_statusupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.CurrentStatus'])),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Resource'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('directory', ['StatusUpdate'])


    def backwards(self, orm):
        # Deleting model 'LongtermStatus'
        db.delete_table('directory_longtermstatus')

        # Deleting model 'CurrentStatus'
        db.delete_table('directory_currentstatus')

        # Deleting model 'Tag'
        db.delete_table('directory_tag')

        # Deleting model 'Contact'
        db.delete_table('directory_contact')

        # Deleting model 'Location'
        db.delete_table('directory_location')

        # Deleting model 'Resource'
        db.delete_table('directory_resource')

        # Removing M2M table for field tags on 'Resource'
        db.delete_table('directory_resource_tags')

        # Deleting model 'StatusUpdate'
        db.delete_table('directory_statusupdate')


    models = {
        'directory.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'directory.currentstatus': {
            'Meta': {'object_name': 'CurrentStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street_one': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'street_two': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'directory.longtermstatus': {
            'Meta': {'object_name': 'LongtermStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permanent': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'directory.resource': {
            'Meta': {'object_name': 'Resource'},
            'affordable_housing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bike_repair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'career_center': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'case_management': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clothing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'computer_center': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contacts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Contact']", 'null': 'True', 'blank': 'True'}),
            'current_status': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.CurrentStatus']", 'null': 'True', 'through': "orm['directory.StatusUpdate']", 'blank': 'True'}),
            'dental': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drop_in': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drug_rehab': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'education_training': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'father_and_child': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'health_center': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_attire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_training': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'laundry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'locations': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']", 'null': 'True', 'blank': 'True'}),
            'longterm_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.LongtermStatus']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'mail_pickup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'men': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mental_health': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mother_and_child': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'showers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_services': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Tag']", 'null': 'True', 'blank': 'True'}),
            'telephones': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transitional_housing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transportation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wheelchair_repair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'women': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'directory.statusupdate': {
            'Meta': {'object_name': 'StatusUpdate'},
            'current_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.CurrentStatus']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Resource']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'directory.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['directory']