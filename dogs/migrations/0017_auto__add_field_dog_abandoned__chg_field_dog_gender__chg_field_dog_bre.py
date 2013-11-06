# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dog.abandoned'
        db.add_column(u'dogs_dog', 'abandoned',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Dog.gender'
        db.alter_column(u'dogs_dog', 'gender', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Dog.breed'
        db.alter_column(u'dogs_dog', 'breed_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.Breed'], null=True))

        # Changing field 'Dog.birth_date'
        db.alter_column(u'dogs_dog', 'birth_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Dog.name'
        db.alter_column(u'dogs_dog', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):
        # Deleting field 'Dog.abandoned'
        db.delete_column(u'dogs_dog', 'abandoned')


        # Changing field 'Dog.gender'
        db.alter_column(u'dogs_dog', 'gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=2))

        # Changing field 'Dog.breed'
        db.alter_column(u'dogs_dog', 'breed_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['dogs.Breed']))

        # Changing field 'Dog.birth_date'
        db.alter_column(u'dogs_dog', 'birth_date', self.gf('django.db.models.fields.DateField')(default=0))

        # Changing field 'Dog.name'
        db.alter_column(u'dogs_dog', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

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
            'apartment': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighbourhood': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'abandoned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adopted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adopted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'adopted_by'", 'null': 'True', 'to': u"orm['dogs.Person']"}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'breed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Breed']", 'null': 'True'}),
            'characteristics': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dogs.Characteristics']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_adoption_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_adoption_by'", 'to': u"orm['dogs.Person']"}),
            'in_adoption_process': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'related_dog': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related_dog'", 'null': 'True', 'to': u"orm['dogs.Dog']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'dogs.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Address']", 'null': 'True', 'blank': 'True'}),
            'answers': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dogs.Answer']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dogs']