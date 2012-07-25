# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tags.flag_enabled'
        db.delete_column('blog_tags', 'flag_enabled')


    def backwards(self, orm):
        # Adding field 'Tags.flag_enabled'
        db.add_column('blog_tags', 'flag_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'categ': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'}),
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Tags']", 'symmetrical': 'False'})
        },
        'blog.tags': {
            'Meta': {'object_name': 'Tags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']