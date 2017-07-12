# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('grant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Grant'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('protect_papers', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('protect_data', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('protect_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field people on 'Project'
        m2m_table_name = db.shorten_name('projects_project_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('person', models.ForeignKey(orm['people.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'person_id'])

        # Adding M2M table for field papers on 'Project'
        m2m_table_name = db.shorten_name('projects_project_papers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('paper', models.ForeignKey(orm['papers.paper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'paper_id'])

        # Adding model 'Grant'
        db.create_table('projects_grant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grant_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('projects', ['Grant'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field people on 'Project'
        db.delete_table(db.shorten_name('projects_project_people'))

        # Removing M2M table for field papers on 'Project'
        db.delete_table(db.shorten_name('projects_project_papers'))

        # Deleting model 'Grant'
        db.delete_table('projects_grant')


    models = {
        'papers.paper': {
            'Meta': {'ordering': "['title']", 'object_name': 'Paper'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Person']", 'symmetrical': 'False'}),
            'code': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'paper': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Category']"}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'projects.grant': {
            'Meta': {'object_name': 'Grant'},
            'grant_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'projects.project': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Project'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'grant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Grant']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'papers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['papers.Paper']", 'symmetrical': 'False', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['people.Person']", 'null': 'True', 'blank': 'True'}),
            'protect_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'protect_data': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'protect_papers': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['projects']