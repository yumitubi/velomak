# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table(u'blog_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.CharField')(max_length=64, unique=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['Section'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categ', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Section'], null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding model 'Tags'
        db.create_table(u'blog_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Tags'])

        # Adding model 'Posts'
        db.create_table(u'blog_posts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('post', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('prepost', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('date_pub', self.gf('django.db.models.fields.DateTimeField')()),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('flag_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('not_publicate_main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Section'], null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Posts'])

        # Adding M2M table for field tags on 'Posts'
        db.create_table(u'blog_posts_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('posts', models.ForeignKey(orm[u'blog.posts'], null=False)),
            ('tags', models.ForeignKey(orm[u'blog.tags'], null=False))
        ))
        db.create_unique(u'blog_posts_tags', ['posts_id', 'tags_id'])

        # Adding model 'Files'
        db.create_table(u'blog_files', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('discription', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('files', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Files'])

        # Adding model 'Comms'
        db.create_table(u'blog_comms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Posts'])),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('datatime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('delete', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['Comms'])

        # Adding model 'Capcha'
        db.create_table(u'blog_capcha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture_name', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('capcha_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('use', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['Capcha'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table(u'blog_section')

        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting model 'Tags'
        db.delete_table(u'blog_tags')

        # Deleting model 'Posts'
        db.delete_table(u'blog_posts')

        # Removing M2M table for field tags on 'Posts'
        db.delete_table('blog_posts_tags')

        # Deleting model 'Files'
        db.delete_table(u'blog_files')

        # Deleting model 'Comms'
        db.delete_table(u'blog_comms')

        # Deleting model 'Capcha'
        db.delete_table(u'blog_capcha')


    models = {
        u'blog.capcha': {
            'Meta': {'object_name': 'Capcha'},
            'capcha_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'use': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'blog.category': {
            'Meta': {'ordering': "['-weight']", 'object_name': 'Category'},
            'categ': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Section']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'blog.comms': {
            'Meta': {'ordering': "['datatime']", 'object_name': 'Comms'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'datatime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Posts']"})
        },
        u'blog.files': {
            'Meta': {'object_name': 'Files'},
            'discription': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'files': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blog.posts': {
            'Meta': {'ordering': "['-date_pub']", 'object_name': 'Posts'},
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            'date_pub': ('django.db.models.fields.DateTimeField', [], {}),
            'flag_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'not_publicate_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'prepost': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Section']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Tags']", 'symmetrical': 'False'})
        },
        u'blog.section': {
            'Meta': {'ordering': "['weight']", 'object_name': 'Section'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'blog.tags': {
            'Meta': {'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']