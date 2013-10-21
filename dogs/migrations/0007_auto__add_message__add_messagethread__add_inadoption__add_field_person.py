# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'dogs_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.MessageThread'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['dogs.Person'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['dogs.Person'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'dogs', ['Message'])

        # Adding model 'MessageThread'
        db.create_table(u'dogs_messagethread', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('person1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person1', to=orm['dogs.Person'])),
            ('person2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person2', to=orm['dogs.Person'])),
        ))
        db.send_create_signal(u'dogs', ['MessageThread'])

        # Adding model 'InAdoption'
        db.create_table(u'dogs_inadoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('adopter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adopter', to=orm['dogs.Person'])),
            ('donator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donator', to=orm['dogs.Person'])),
            ('dog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.Dog'])),
        ))
        db.send_create_signal(u'dogs', ['InAdoption'])

        # Adding field 'Person.tel'
        db.add_column(u'dogs_person', 'tel',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'dogs_message')

        # Deleting model 'MessageThread'
        db.delete_table(u'dogs_messagethread')

        # Deleting model 'InAdoption'
        db.delete_table(u'dogs_inadoption')

        # Deleting field 'Person.tel'
        db.delete_column(u'dogs_person', 'tel')


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
            'apartment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'dogs.inadoption': {
            'Meta': {'object_name': 'InAdoption'},
            'adopter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adopter'", 'to': u"orm['dogs.Person']"}),
            'dog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Dog']"}),
            'donator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donator'", 'to': u"orm['dogs.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dogs.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': u"orm['dogs.Person']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': u"orm['dogs.Person']"}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.MessageThread']"})
        },
        u'dogs.messagethread': {
            'Meta': {'object_name': 'MessageThread'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person1'", 'to': u"orm['dogs.Person']"}),
            'person2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person2'", 'to': u"orm['dogs.Person']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'dogs.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Address']", 'null': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dogs']