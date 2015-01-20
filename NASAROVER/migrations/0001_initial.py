# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grid'
        db.create_table(u'NASAROVER_grid', (
            ('Grid_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('breadth', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'NASAROVER', ['Grid'])

        # Adding model 'rover'
        db.create_table(u'NASAROVER_rover', (
            ('rover_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rover_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rover_ownedby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'NASAROVER', ['rover'])

        # Adding model 'subgrid'
        db.create_table(u'NASAROVER_subgrid', (
            ('Grid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Grid'])),
            ('grid_x', self.gf('django.db.models.fields.IntegerField')()),
            ('grid_y', self.gf('django.db.models.fields.IntegerField')()),
            ('subgrid_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'NASAROVER', ['subgrid'])

        # Adding model 'Mineral'
        db.create_table(u'NASAROVER_mineral', (
            ('Name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('M_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'NASAROVER', ['Mineral'])

        # Adding model 'MineralDistribution'
        db.create_table(u'NASAROVER_mineraldistribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Grid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Grid'])),
            ('subgrid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.subgrid'])),
            ('m_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Mineral'])),
            ('quanity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'NASAROVER', ['MineralDistribution'])

        # Adding model 'roversensor'
        db.create_table(u'NASAROVER_roversensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rover_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.rover'])),
            ('m_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.Mineral'])),
        ))
        db.send_create_signal(u'NASAROVER', ['roversensor'])

        # Adding model 'rover_position'
        db.create_table(u'NASAROVER_rover_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Grid_id', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['NASAROVER.rover'])),
            ('rover_x', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_y', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_direction', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'NASAROVER', ['rover_position'])


    def backwards(self, orm):
        # Deleting model 'Grid'
        db.delete_table(u'NASAROVER_grid')

        # Deleting model 'rover'
        db.delete_table(u'NASAROVER_rover')

        # Deleting model 'subgrid'
        db.delete_table(u'NASAROVER_subgrid')

        # Deleting model 'Mineral'
        db.delete_table(u'NASAROVER_mineral')

        # Deleting model 'MineralDistribution'
        db.delete_table(u'NASAROVER_mineraldistribution')

        # Deleting model 'roversensor'
        db.delete_table(u'NASAROVER_roversensor')

        # Deleting model 'rover_position'
        db.delete_table(u'NASAROVER_rover_position')


    models = {
        u'NASAROVER.grid': {
            'Grid_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'object_name': 'Grid'},
            'breadth': ('django.db.models.fields.IntegerField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {})
        },
        u'NASAROVER.mineral': {
            'M_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'object_name': 'Mineral'},
            'Name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'NASAROVER.mineraldistribution': {
            'Grid_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Grid']"}),
            'Meta': {'object_name': 'MineralDistribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Mineral']"}),
            'quanity': ('django.db.models.fields.IntegerField', [], {}),
            'subgrid_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.subgrid']"})
        },
        u'NASAROVER.rover': {
            'Meta': {'object_name': 'rover'},
            'rover_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rover_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rover_ownedby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'NASAROVER.rover_position': {
            'Grid_id': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'rover_position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rover_direction': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'rover_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.rover']"}),
            'rover_x': ('django.db.models.fields.IntegerField', [], {}),
            'rover_y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'NASAROVER.roversensor': {
            'Meta': {'object_name': 'roversensor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Mineral']"}),
            'rover_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.rover']"})
        },
        u'NASAROVER.subgrid': {
            'Grid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['NASAROVER.Grid']"}),
            'Meta': {'object_name': 'subgrid'},
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