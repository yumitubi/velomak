# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table('blog_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('blog', ['Section'])

        # Adding field 'Posts.section'
        db.add_column('blog_posts', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='test', to=orm['blog.Section']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table('blog_section')

        # Deleting field 'Posts.section'
        db.delete_column('blog_posts', 'section_id')


    models = {
        'blog.category': {
            'Meta': {'ordering': "['-weight']", 'object_name': 'Category'},
            'categ': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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
            'date_pub': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'flag_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'prepost': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Section']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Tags']", 'symmetrical': 'False'})
        },
        'blog.section': {
            'Meta': {'ordering': "['weight']", 'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'blog.tags': {
            'Meta': {'object_name': 'Tags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']