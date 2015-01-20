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
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('direct', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rover_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
            'direct': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rover_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
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
        }
    }

    complete_apps = ['NASAROVER']