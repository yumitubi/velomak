# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Posts.date_pub'
        db.alter_column('blog_posts', 'date_pub', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Posts.date_pub'
        db.alter_column('blog_posts', 'date_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        'blog.capcha': {
            'Meta': {'object_name': 'Capcha'},
            'capcha_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'use': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'blog.category': {
            'Meta': {'ordering': "['-weight']", 'object_name': 'Category'},
            'categ': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Section']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'blog.comms': {
            'Meta': {'ordering': "['datatime']", 'object_name': 'Comms'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'datatime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Posts']"})
        },
        'blog.files': {
            'Meta': {'object_name': 'Files'},
            'discription': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'files': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'blog.posts': {
            'Meta': {'ordering': "['-date_pub']", 'object_name': 'Posts'},
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {}),
            'flag_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'not_publicate_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'prepost': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Section']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Tags']", 'symmetrical': 'False'})
        },
        'blog.section': {
            'Meta': {'ordering': "['weight']", 'object_name': 'Section'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'blog.tags': {
            'Meta': {'object_name': 'Tags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']