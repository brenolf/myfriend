 #!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Address(models.Model):
    # precisa ter telefone de contato também
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    apartment = models.CharField(max_length=50)
    neighbourhood = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    STATE_CHOICES = (("AC", "Acre"),
                    ("AL", "Alagoas"),
                    ("AP", "Amapá"),
                    ("AM", "Amazonas"),
                    ("BA", "Bahia",),
                    ("CE", "Ceará"),
                    ("DF", "Distrito Federal"),
                    ("ES", "Espírito Santo"),
                    ("GO", "Goiás"),
                    ("MA", "Maranhão"),
                    ("MT", "Mato Grosso"),
                    ("MS", "Mato Grosso do Sul"),
                    ("MG", "Minas Gerais"),
                    ("PA", "Pará"),
                    ("PB", "Paraíba"),
                    ("PR", "Paraná"),
                    ("PE", "Pernambuco"),
                    ("PI", "Piauí"),
                    ("RJ", "Rio de Janeiro"),
                    ("RN", "Rio Grande do Norte"),
                    ("RS", "Rio Grande do Sul"),
                    ("RO", "Rondônia"),
                    ("RR", "Roraima"),
                    ("SC", "Santa Catarina"),
                    ("SP", "São Paulo"),
                    ("SE", "Sergipe"),
                    ("TO", "Tocantins"))
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    postal_code = models.CharField(max_length=9)  # colocar validação


class Breed(models.Model):
    breed_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.breed_name
    # aqui precisa ser limitado


class Person(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField()
    SEX_CHOICES = (("M", "Masculino"), ("F", "Feminino"))
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    address = models.ForeignKey(Address)

    def __unicode__(self):
        return self.user.username
    #answers = models.OneToOneField(Answer)


class Dog(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField('data de nascimento aproximada')
    # complementar
    SIZE_CHOICES = (("P", "Pequeno"), ("M", "Médio"), ("G", "Grande"))
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    description = models.TextField()
    GENDER_CHOICES = (("M", "Macho"), ("F", "Fêmea"))
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed)
    # A ideia é que um cachorro seja associado a um endereço da pessoa,
    # e não à pessoa. Se quiser ser associada a ela, é só
    # colocar que o endereço do cachorro é o mesmo que o dela, e eles vão
    # ficar sincronizados
    address = models.ForeignKey(Address)
    adopted = models.BooleanField()
    adopted_by = models.ForeignKey(
        Person, related_name="adopted_by", null=True)
    in_adoption_by = models.ForeignKey(Person, related_name="in_adoption_by")

    def __unicode__(self):
        return self.name


class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['address']


class DogForm(ModelForm):

    class Meta:
        model = Dog
        exclude = ['address', 'adopted', 'adopted_by', 'in_adoption_by']


class AddressForm(ModelForm):

    class Meta:
        model = Address




# class Characteristic(models.Model):
    # aqui também precisa ser limitado, são características "imposed"
    # perguntadas

# class Album(models.Model): #many photos and videos

# class Photo(models.Model):

# class Video(models.Model):


# class Answers(models.Model):

    # conjunto de true/none/false também
