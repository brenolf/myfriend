 #!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# segundo o próprio site do python, é o melhor lugar pra colocar signals, mas wtf hein?
# tentar achar lugar melhor
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def after_sign_up(sender, **kwargs):
    request = kwargs['request']
    user = kwargs['user']
    p = Person()
    user.person = p
    user.save()
    p.user = user
    p.save()


class Address(models.Model):
    # precisa ter telefone de contato também
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    apartment = models.CharField(max_length=50, null=True)
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
    birth_date = models.DateField(null=True)
    GENDER_CHOICES = (("M", "Masculino"), ("F", "Feminino"))
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    address = models.ForeignKey(Address, null=True)
    tel = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.user.username
    #answers = models.OneToOneField(Answer)


class Dog(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField('data de nascimento aproximada')
    # complementar
    SIZE_CHOICES = (("xs", "Muito Pequeno"), ("s", "Pequeno"),
                    ("m", "Médio"), ("l", "Grande"), ("xl", "Muito Grande"))
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    description = models.TextField()
    GENDER_CHOICES = (("M", "Macho"), ("F", "Fêmea"))
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    COLOR_CHOICES = (
        ("bl", "Preto"),
        ("ma", "Marrom"),
        ("wh", "Branco"),
        ("gr", "Cinza"),
        ("go", "Dourado"),
        ("bw", "Preto/Branco"),
    )
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    breed = models.ForeignKey(Breed)
    # A ideia é que um cachorro seja associado a um endereço da pessoa,
    # e não à pessoa. Se quiser ser associada a ela, é só
    # colocar que o endereço do cachorro é o mesmo que o dela, e eles vão
    # ficar sincronizados
    photo = models.ImageField(null=True, upload_to="dog_images/")
    adopted = models.BooleanField()
    adopted_by = models.ForeignKey(
        Person, related_name="adopted_by", null=True)
    in_adoption_by = models.ForeignKey(Person, related_name="in_adoption_by")

    def __unicode__(self):
        return self.name

# Classe usada para processo de adocao
class InAdoption(models.Model):
    adopter = models.ForeignKey(Person,related_name="adopter")
    dog = models.ForeignKey(Dog)

class MessageThread(models.Model):
    subject = models.CharField(max_length=50)
    person1 = models.ForeignKey(Person,related_name="person1")
    person2 = models.ForeignKey(Person,related_name="person2")
    related_dog = models.ForeignKey(Dog, related_name="related_dog", null=True)
    

class Message(models.Model):
    thread = models.ForeignKey(MessageThread)
    sender = models.ForeignKey(Person,related_name="sender")
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)


class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['address', 'user']


class InAdoptionForm(ModelForm):

    class Meta:
        model = InAdoption

class DogForm(ModelForm):

    class Meta:
        model = Dog
        #photo = models.ImageField(upload_to = 'dog_images/', default = 'dog_images/None/no-img.jpg')
        exclude = ['address', 'adopted', 'adopted_by', 'in_adoption_by']


class AddressForm(ModelForm):

    class Meta:
        model = Address


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']




# class Characteristic(models.Model):
    # aqui também precisa ser limitado, são características "imposed"
    # perguntadas

# class Album(models.Model): #many photos and videos

# class Photo(models.Model):

# class Video(models.Model):


# class Answers(models.Model):

    # conjunto de true/none/false também
