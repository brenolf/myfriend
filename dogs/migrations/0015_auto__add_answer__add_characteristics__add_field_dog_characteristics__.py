# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table(u'dogs_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apartment', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('backyard', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('insidehouse', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('smalldogs', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('manyguests', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('priorexperience', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('training', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('physicallyactive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('calmness', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('likebarks', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('likeaggressiveness', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('likewalking', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('havemoney', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('allergy', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('smallanimals', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('otheranimals', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('kids', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dogs', ['Answer'])

        # Adding model 'Characteristics'
        db.create_table(u'dogs_characteristics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('calm', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('barker', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('longhair', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('needexercise', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('stubborn', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('expensive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('medicalcare', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('aggressive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('jealousanimal', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('jealousperson', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('hunter', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('likekids', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('hairfall', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('likeoutside', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('likeinside', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dogs', ['Characteristics'])

        # Adding field 'Dog.characteristics'
        db.add_column(u'dogs_dog', 'characteristics',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dogs.Characteristics'], unique=True, null=True),
                      keep_default=False)

        # Adding field 'Person.answers'
        db.add_column(u'dogs_person', 'answers',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dogs.Answer'], unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table(u'dogs_answer')

        # Deleting model 'Characteristics'
        db.delete_table(u'dogs_characteristics')

        # Deleting field 'Dog.characteristics'
        db.delete_column(u'dogs_dog', 'characteristics_id')

        # Deleting field 'Person.answers'
        db.delete_column(u'dogs_person', 'answers_id')


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
        u'dogs.answer': {
            'Meta': {'object_name': 'Answer'},
            'allergy': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'apartment': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'backyard': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'calmness': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'havemoney': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insidehouse': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'kids': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likeaggressiveness': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likebarks': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likewalking': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'manyguests': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'otheranimals': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'physicallyactive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'priorexperience': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'smallanimals': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'smalldogs': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dogs.breed': {
            'Meta': {'object_name': 'Breed'},
            'breed_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dogs.characteristics': {
            'Meta': {'object_name': 'Characteristics'},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'aggressive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'barker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'calm': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'expensive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hairfall': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hunter': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jealousanimal': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'jealousperson': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likeinside': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likekids': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likeoutside': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'longhair': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'medicalcare': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'needexercise': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'stubborn': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dogs.dog': {
            'Meta': {'object_name': 'Dog'},
            'adopted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adopted_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adopted_by'", 'null': 'True', 'to': u"orm['dogs.Person']"}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'breed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Breed']"}),
            'characteristics': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dogs.Characteristics']", 'unique': 'True', 'null': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_adoption_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_adoption_by'", 'to': u"orm['dogs.Person']"}),
            'in_adoption_process': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'dogs.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': u"orm['dogs.Person']"}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.MessageThread']"})
        },
        u'dogs.messagethread': {
            'Meta': {'object_name': 'MessageThread'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person1'", 'to': u"orm['dogs.Person']"}),
            'person2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person2'", 'to': u"orm['dogs.Person']"}),
            'related_dog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_dog'", 'null': 'True', 'to': u"orm['dogs.Dog']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'dogs.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Address']", 'null': 'True'}),
            'answers': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dogs.Answer']", 'unique': 'True', 'null': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dogs']