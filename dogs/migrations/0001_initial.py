# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'dogs_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('apartment', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('neighbourhood', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal(u'dogs', ['Address'])

        # Adding model 'Breed'
        db.create_table(u'dogs_breed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('breed_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'dogs', ['Breed'])

        # Adding model 'Person'
        db.create_table(u'dogs_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.Address'])),
        ))
        db.send_create_signal(u'dogs', ['Person'])

        # Adding model 'Dog'
        db.create_table(u'dogs_dog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('breed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.Breed'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.Address'])),
            ('adopted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adopted_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adopted_by', null=True, to=orm['dogs.Person'])),
            ('in_adoption_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='in_adoption_by', to=orm['dogs.Person'])),
        ))
        db.send_create_signal(u'dogs', ['Dog'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'dogs_address')

        # Deleting model 'Breed'
        db.delete_table(u'dogs_breed')

        # Deleting model 'Person'
        db.delete_table(u'dogs_person')

        # Deleting model 'Dog'
        db.delete_table(u'dogs_dog')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dogs.address': {
            'Meta': {'object_name': 'Address'},
            'apartment': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighbourhood': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'dogs.breed': {
            'Meta': {'object_name': 'Breed'},
            'breed_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dogs.dog': {
            'Meta': {'object_name': 'Dog'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Address']"}),
            'adopted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adopted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adopted_by'", 'null': 'True', 'to': u"orm['dogs.Person']"}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'breed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Breed']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_adoption_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_adoption_by'", 'to': u"orm['dogs.Person']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'dogs.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Address']"}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dogs']