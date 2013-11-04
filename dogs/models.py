 #!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# segundo o próprio site do python, é o melhor lugar pra colocar signals, mas wtf hein?
# tentar achar lugar melhor
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


@receiver(user_signed_up)
def after_sign_up(sender, **kwargs):
    request = kwargs['request']
    user = kwargs['user']
    p = Person()
    user.person = p
    user.save()
    if 'first_name' in request:
        p.first_name = request['first_name']
    if 'last_name' in request:
        p.last_name = request['last_name']
    p.user = user
    a = Answer()
    a.save()
    p.answers=a
    p.save()
    user.save()
    print 'passou aquiiiiii'
    messages.warning(request, "Você pode completar o cadastro agora, ou mais tarde acessando sua página de usuário e clicando em editar")
    return HttpResponseRedirect('persons/create.html')


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

class Answer(models.Model):
    #no index, se algo daqui for null, só desconsiderar o campo na hora de dividir pelo total
    #ja se algo do cão for null, talvez somar 0.5 no total pra dividir (pra representar que
    #null é "mais fraco" que "no", ou seja, vai diminuir menos o indice
    apartment = models.NullBooleanField() #mora em apartamento/problema de espaço?
    backyard = models.NullBooleanField() #tem um quintal de tamanho decente?
    insidehouse = models.NullBooleanField() #prefere cães que vão ficar dentro de casa?
    smalldogs = models.NullBooleanField() #prefere cachorros pequenos?
    manyguests = models.NullBooleanField() #vai receber muitas visitas?
    priorexperience = models.NullBooleanField() #experiencia anterior?
    time = models.NullBooleanField() #tem tempo disponivel? para grooming e tal /pelos grandes
    training = models.NullBooleanField() #pretende treinar o cão?
    physicallyactive = models.NullBooleanField() #é ativo fisicamente?
    calmness = models.NullBooleanField() #é calmo? Para cuidar de cães que dão trabalho
    likebarks = models.NullBooleanField() #não liga para cães que gostam de latir?
    likeaggressiveness = models.NullBooleanField() #não liga pra cães mais agressivos?
    likewalking = models.NullBooleanField() #gosta de passear com o cão?
    havemoney = models.NullBooleanField() #não liga de gastar com o cão?
    allergy = models.NullBooleanField() #tem problemas com pelos?
    smallanimals = models.NullBooleanField() #tem outros animais pequenos?
    otheranimals = models.NullBooleanField() #tem outros animais
    kids = models.NullBooleanField()  #tem crianças?

class Person(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField(null=True)
    GENDER_CHOICES = (("M", "Masculino"), ("F", "Feminino"))
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    address = models.ForeignKey(Address, null=True)
    tel = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.user.username
    answers = models.OneToOneField(Answer, default=Answer(), null=True)



class Characteristics(models.Model):
    active = models.NullBooleanField() #muito ativo
    calm = models.NullBooleanField() #bem calmo
    barker = models.NullBooleanField() #gosta de latir
    longhair = models.NullBooleanField() #tem muitos cabelos
    needexercise = models.NullBooleanField() #precisa/gosta de exercícios
    stubborn = models.NullBooleanField() #teimoso/precisa de treino
    #young = models.NullBooleanField() #bom setar dependendo da data
    expensive = models.NullBooleanField() #precisa de comida cara/atenção
    medicalcare = models.NullBooleanField() #tem algum problema e precisa de cuidados médicos
    aggressive = models.NullBooleanField() #é agressivo
    jealousanimal = models.NullBooleanField() #tem ciumes de outros cães/animais
    jealousperson = models.NullBooleanField()  #ciumes de pessoas
    hunter = models.NullBooleanField() #gosta de caçar outros animais
    likekids = models.NullBooleanField() #gosta de crianças
    hairfall = models.NullBooleanField() #os pelos caem
    likeoutside = models.NullBooleanField() #gosta de ar livre
    likeinside = models.NullBooleanField() #gosta de ficar dentro do apartamento


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
    adopted = models.BooleanField() # ja foi adotado
    adopted_by = models.ForeignKey(Person, related_name="adopted_by", null=True) # quem adotou
    in_adoption_by = models.ForeignKey(Person, related_name="in_adoption_by") # quem pos para adocao
    in_adoption_process = models.BooleanField() # em estado de adocao
    characteristics= models.OneToOneField(Characteristics, default=Characteristics(), null=True)

    def __unicode__(self):
        return self.name


class MessageThread(models.Model):
    subject = models.CharField(max_length=50)
    person1 = models.ForeignKey(Person,related_name="person1")
    person2 = models.ForeignKey(Person,related_name="person2")
    related_dog = models.ForeignKey(Dog, related_name="related_dog", null=True)
    date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField()


class Message(models.Model):
    thread = models.ForeignKey(MessageThread)
    sender = models.ForeignKey(Person,related_name="sender")
    content = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

class MessageForm(ModelForm):

    class Meta:
        model = Message
        exclude = ['thread', 'sender', 'date']

class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['address', 'user']

class DogForm(ModelForm):

    class Meta:
        model = Dog
        #photo = models.ImageField(upload_to = 'dog_images/', default = 'dog_images/None/no-img.jpg')
        exclude = ['address', 'adopted', 'adopted_by', 'in_adoption_by', 'in_adoption_process']


class AddressForm(ModelForm):

    class Meta:
        model = Address


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class AnswerForm(ModelForm):

    class Meta:
        model = Answer

class CharacteristicsForm(ModelForm):

    class Meta:
        model = Characteristics




# class Characteristic(models.Model):
    # aqui também precisa ser limitado, são características "imposed"
    # perguntadas

# class Album(models.Model): #many photos and videos

# class Photo(models.Model):

# class Video(models.Model):


# class Answers(models.Model):

    # conjunto de true/none/false também
