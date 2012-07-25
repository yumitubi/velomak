# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Posts.tags'
        db.delete_column('blog_posts', 'tags')

        # Adding M2M table for field tags on 'Posts'
        db.create_table('blog_posts_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('posts', models.ForeignKey(orm['blog.posts'], null=False)),
            ('tags', models.ForeignKey(orm['blog.tags'], null=False))
        ))
        db.create_unique('blog_posts_tags', ['posts_id', 'tags_id'])

        # Deleting field 'Tags.tags'
        db.delete_column('blog_tags', 'tags')

        # Adding field 'Tags.tag'
        db.add_column('blog_tags', 'tag',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=64, blank=True),
                      keep_default=False)


        # Changing field 'Category.categ'
        db.alter_column('blog_category', 'categ', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=64))
        # Adding unique constraint on 'Category', fields ['categ']
        db.create_unique('blog_category', ['categ'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['categ']
        db.delete_unique('blog_category', ['categ'])

        # Adding field 'Posts.tags'
        db.add_column('blog_posts', 'tags',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Removing M2M table for field tags on 'Posts'
        db.delete_table('blog_posts_tags')

        # Adding field 'Tags.tags'
        db.add_column('blog_tags', 'tags',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Tags.tag'
        db.delete_column('blog_tags', 'tag')


        # Changing field 'Category.categ'
        db.alter_column('blog_category', 'categ', self.gf('django.db.models.fields.TextField')(null=True))

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
            'flag_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']