# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grid'
        db.create_table(u'NASAROVER_grid', (
            ('grid_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('breadth', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'NASAROVER', ['Grid'])

        # Adding model 'Rover'
        db.create_table(u'NASAROVER_rover', (
            ('rover_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rover_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rover_ownedby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'NASAROVER', ['Rover'])

        # Adding model 'Subgrid'
        db.create_table(u'NASAROVER_subgrid', (
            ('grid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Grid'])),
            ('grid_x', self.gf('django.db.models.fields.IntegerField')()),
            ('grid_y', self.gf('django.db.models.fields.IntegerField')()),
            ('subgrid_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'NASAROVER', ['Subgrid'])

        # Adding model 'Mineral'
        db.create_table(u'NASAROVER_mineral', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('m_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'NASAROVER', ['Mineral'])

        # Adding model 'MineralDistribution'
        db.create_table(u'NASAROVER_mineraldistribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Grid'])),
            ('subgrid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Subgrid'])),
            ('m_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Mineral'])),
            ('quanity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'NASAROVER', ['MineralDistribution'])

        # Adding model 'Roversensor'
        db.create_table(u'NASAROVER_roversensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rover_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Rover'])),
            ('m_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Mineral'])),
        ))
        db.send_create_signal(u'NASAROVER', ['Roversensor'])

        # Adding unique constraint on 'Roversensor', fields ['rover_id', 'm_id']
        db.create_unique(u'NASAROVER_roversensor', ['rover_id_id', 'm_id_id'])

        # Adding model 'Roverposition'
        db.create_table(u'NASAROVER_roverposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grid_id', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Rover'])),
            ('rover_x', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_y', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_direction', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'NASAROVER', ['Roverposition'])


    def backwards(self, orm):
        # Removing unique constraint on 'Roversensor', fields ['rover_id', 'm_id']
        db.delete_unique(u'NASAROVER_roversensor', ['rover_id_id', 'm_id_id'])

        # Deleting model 'Grid'
        db.delete_table(u'NASAROVER_grid')

        # Deleting model 'Rover'
        db.delete_table(u'NASAROVER_rover')

        # Deleting model 'Subgrid'
        db.delete_table(u'NASAROVER_subgrid')

        # Deleting model 'Mineral'
        db.delete_table(u'NASAROVER_mineral')

        # Deleting model 'MineralDistribution'
        db.delete_table(u'NASAROVER_mineraldistribution')

        # Deleting model 'Roversensor'
        db.delete_table(u'NASAROVER_roversensor')

        # Deleting model 'Roverposition'
        db.delete_table(u'NASAROVER_roverposition')


    models = {
        u'NASAROVER.grid': {
            'Meta': {'object_name': 'Grid'},
            'breadth': ('django.db.models.fields.IntegerField', [], {}),
            'grid_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {})
        },
        u'NASAROVER.mineral': {
            'Meta': {'object_name': 'Mineral'},
            'm_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'NASAROVER.mineraldistribution': {
            'Meta': {'object_name': 'MineralDistribution'},
            'grid_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Grid']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Mineral']"}),
            'quanity': ('django.db.models.fields.IntegerField', [], {}),
            'subgrid_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Subgrid']"})
        },
        u'NASAROVER.rover': {
            'Meta': {'object_name': 'Rover'},
            'rover_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rover_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rover_ownedby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'NASAROVER.roverposition': {
            'Meta': {'object_name': 'Roverposition'},
            'grid_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rover_direction': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'rover_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Rover']"}),
            'rover_x': ('django.db.models.fields.IntegerField', [], {}),
            'rover_y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'NASAROVER.roversensor': {
            'Meta': {'unique_together': "(('rover_id', 'm_id'),)", 'object_name': 'Roversensor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Mineral']"}),
            'rover_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Rover']"})
        },
        u'NASAROVER.subgrid': {
            'Meta': {'object_name': 'Subgrid'},
            'grid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Grid']"}),
            'grid_x': ('django.db.models.fields.IntegerField', [], {}),
            'grid_y': ('django.db.models.fields.IntegerField', [], {}),
            'subgrid_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['NASAROVER']