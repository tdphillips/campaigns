# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prospectus'
        db.create_table(u'campaign_prospectus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('privacy_status', self.gf('django.db.models.fields.CharField')(default='PR', max_length=2)),
            ('private_votes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vote_type', self.gf('django.db.models.fields.CharField')(default='RANK', max_length=10)),
            ('point_multiplier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'campaign', ['Prospectus'])

        # Adding model 'Campaign'
        db.create_table(u'campaign_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prospectus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Prospectus'])),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'campaign', ['Campaign'])

        # Adding model 'Vote'
        db.create_table(u'campaign_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'campaign', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Prospectus'
        db.delete_table(u'campaign_prospectus')

        # Deleting model 'Campaign'
        db.delete_table(u'campaign_campaign')

        # Deleting model 'Vote'
        db.delete_table(u'campaign_vote')


    models = {
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
        u'campaign.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prospectus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Prospectus']"})
        },
        u'campaign.prospectus': {
            'Meta': {'object_name': 'Prospectus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'point_multiplier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'privacy_status': ('django.db.models.fields.CharField', [], {'default': "'PR'", 'max_length': '2'}),
            'private_votes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vote_type': ('django.db.models.fields.CharField', [], {'default': "'RANK'", 'max_length': '10'})
        },
        u'campaign.vote': {
            'Meta': {'object_name': 'Vote'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['campaign']