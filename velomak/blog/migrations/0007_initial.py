# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categ', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Category'])

        # Adding model 'Posts'
        db.create_table('blog_posts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('post', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('prepost', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('flag_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blog', ['Posts'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('blog_category')

        # Deleting model 'Posts'
        db.delete_table('blog_posts')


    models = {
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'categ': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'blog.posts': {
            'Meta': {'ordering': "['-date_pub']", 'object_name': 'Posts'},
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'date_pub': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'flag_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'prepost': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['blog']