 #!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import TypedChoiceField
from django.forms import RadioSelect
from database_storage import DatabaseStorage

# segundo o próprio site do python, é o melhor lugar pra colocar signals, mas wtf hein?
# tentar achar lugar melhor
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

import datetime
import inspect
from django.core.exceptions import ValidationError

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
	messages.warning(request, "Você pode completar o cadastro agora, ou mais tarde acessando sua página de usuário e clicando em editar")
	return HttpResponseRedirect('persons/create.html')


class Address(models.Model):
	# precisa ter telefone de contato também
	street = models.CharField(max_length=200, null=True, blank=True)
	number = models.CharField(max_length=20, null=True, blank=True)
	apartment = models.CharField(max_length=50, null=True, blank=True)
	neighbourhood = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
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
	state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
	postal_code = models.CharField(max_length=9, null=True, blank=True)  # colocar validação


class Breed(models.Model):
	breed_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.breed_name
	# aqui precisa ser limitado

class Answer(models.Model):
	#no index, se algo daqui for null, só desconsiderar o campo na hora de dividir pelo total
	#ja se algo do cão for null, talvez somar 0.5 no total pra dividir (pra representar que
	#null é "mais fraco" que "no", ou seja, vai diminuir menos o indice
	apartment = models.NullBooleanField(verbose_name='Mora em apartamento, ou tem problema com espaço?') #mora em apartamento/problema de espaço?
	backyard = models.NullBooleanField(verbose_name='Tem um quintal onde o cão possa ficar?') #tem um quintal de tamanho decente?
	insidehouse = models.NullBooleanField(verbose_name='Permite que o cão fique dentro de sua casa?') #prefere cães que vão ficar dentro de casa?
	smalldogs = models.NullBooleanField(verbose_name='Prefere cães pequenos?') #prefere cachorros pequenos?
	manyguests = models.NullBooleanField(verbose_name='Recebe muitas visitas?') #vai receber muitas visitas?
	priorexperience = models.NullBooleanField(verbose_name='Tem experiência anterior?') #experiencia anterior?
	time = models.NullBooleanField(verbose_name='Tem tempo livre para cuidar do cão?') #tem tempo disponivel? para grooming e tal /pelos grandes
	training = models.NullBooleanField(verbose_name='Pretende treinar o cão?') #pretende treinar o cão?
	physicallyactive = models.NullBooleanField(verbose_name='Você é fisicamente ativo? Gosta de fazer exercícios?') #é ativo fisicamente?
	calmness = models.NullBooleanField(verbose_name='Você é calmo? Tem paciência?') #é calmo? Para cuidar de cães que dão trabalho
	likebarks = models.NullBooleanField(verbose_name='Você gosta de cães que gostam de latir?') #não liga para cães que gostam de latir?
	likeaggressiveness = models.NullBooleanField(verbose_name='Você é indiferente ou gosta de ter cães mais agressivos?') #não liga pra cães mais agressivos?
	likewalking = models.NullBooleanField(verbose_name='Você gosta de passear? Passearia com o cão?') #gosta de passear com o cão?
	havemoney = models.NullBooleanField(verbose_name='Você tem dinheiro para gastar com o cão?') #não liga de gastar com o cão?
	allergy = models.NullBooleanField(verbose_name='Você tem alergia ou outros problemas com pelos?') #tem problemas com pelos?
	smallanimals = models.NullBooleanField(verbose_name='Você tem animais pequenos?') #tem outros animais pequenos?
	otheranimals = models.NullBooleanField(verbose_name='Você tem outros cães?') #tem outros animais
	kids = models.NullBooleanField(verbose_name='Você tem crianças na sua casa?')  #tem crianças?

class Person(models.Model):
	user = models.OneToOneField(User)
	birth_date = models.DateField(null=True, blank=True)
	GENDER_CHOICES = (("M", "Masculino"), ("F", "Feminino"))
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
	address = models.ForeignKey(Address, null=True, blank=True)
	tel = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return self.user.username
	answers = models.OneToOneField(Answer, default=Answer(), null=True, blank=True)
	emaildog = models.CharField(max_length=3,null=True, blank=True)



class Characteristics(models.Model):
	active = models.NullBooleanField(verbose_name='O cão é ativo fisicamente?') #muito ativo
	calm = models.NullBooleanField(verbose_name='O cão é calmo?') #bem calmo
	barker = models.NullBooleanField(verbose_name='O cão gosta de latir?') #gosta de latir
	longhair = models.NullBooleanField(verbose_name='O cão tem pelos longos?') #tem muitos cabelos
	needexercise = models.NullBooleanField(verbose_name='O cão precisa se exercitar constantemente?') #precisa/gosta de exercícios
	stubborn = models.NullBooleanField(verbose_name='O cão é teimoso?') #teimoso/precisa de treino
	#young = models.NullBooleanField(verbose_name='') #bom setar dependendo da data
	expensive = models.NullBooleanField(verbose_name='O cão custa muito financeiramente para cuidar?') #precisa de comida cara/atenção
	medicalcare = models.NullBooleanField(verbose_name='O cão tem algum problema de saúde que precisa de cuidado constante?') #tem algum problema e precisa de cuidados médicos
	aggressive = models.NullBooleanField(verbose_name='O cão é agressivo, ou tem histórico de agressividade?') #é agressivo
	jealousanimal = models.NullBooleanField(verbose_name='O cão tem ciúmes de outros animais?') #tem ciumes de outros cães/animais
	jealousperson = models.NullBooleanField(verbose_name='O cão tem ciúmes de pessoas?')  #ciumes de pessoas
	hunter = models.NullBooleanField(verbose_name='O cão gosta de caçar outros animais?') #gosta de caçar outros animais
	likekids = models.NullBooleanField(verbose_name='O cão gosta de crianças?') #gosta de crianças
	hairfall = models.NullBooleanField(verbose_name='O cão solta muitos pelos?') #os pelos caem
	likeoutside = models.NullBooleanField(verbose_name='O cão prefere ar livre?') #gosta de ar livre
	likeinside = models.NullBooleanField(verbose_name='O cão gosta de ficar dentro de casa?') #gosta de ficar dentro do apartamento


DB_FILES = {
	'db_table': 'FILES',
	'fname_column':  'FILE_NAME',
	'blob_column': 'BLOB',
	'size_column': 'SIZE',
	'base_url': '/dog_images/',
}
DBS_OPTIONS = {
		'table': 'FILES',
		'base_url': '/dog_images/',
	}

class Dog(models.Model):
	name = models.CharField(max_length=50, null=True)
	birth_date = models.DateField('data de nascimento aproximada', null=True, blank=True)
	# complementar
	SIZE_CHOICES = (("xs", "Muito Pequeno"), ("s", "Pequeno"),
					("m", "Médio"), ("l", "Grande"), ("xl", "Muito Grande"))
	size = models.CharField(max_length=2, choices=SIZE_CHOICES)
	description = models.TextField()
	GENDER_CHOICES = (("M", "Macho"), ("F", "Fêmea"))
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
	COLOR_CHOICES = (
		("bl", "Preto"),
		("ma", "Marrom"),
		("wh", "Branco"),
		("gr", "Cinza"),
		("go", "Dourado"),
		("bw", "Preto/Branco"),
	)
	color = models.CharField(max_length=50, choices=COLOR_CHOICES)
	breed = models.ForeignKey(Breed, null=True)
	# A ideia é que um cachorro seja associado a um endereço da pessoa,
	# e não à pessoa. Se quiser ser associada a ela, é só
	# colocar que o endereço do cachorro é o mesmo que o dela, e eles vão
	# ficar sincronizados
	photo = models.ImageField(null=True, blank=True, upload_to="dog_images/", storage=DatabaseStorage(DBS_OPTIONS))
	adopted = models.BooleanField() # ja foi adotado
	adopted_by = models.ForeignKey(Person, related_name="adopted_by", null=True, blank=True) # quem adotou
	in_adoption_by = models.ForeignKey(Person, related_name="in_adoption_by") # quem pos para adocao
	in_adoption_process = models.BooleanField() # em estado de adocao
	characteristics= models.OneToOneField(Characteristics, default=Characteristics(), null=True, blank=True)
	abandoned = models.BooleanField()

	def __unicode__(self):
		return self.name


class MessageThread(models.Model):
	subject = models.CharField(max_length=50)
	person1 = models.ForeignKey(Person,related_name="person1")
	person2 = models.ForeignKey(Person,related_name="person2")
	related_dog = models.ForeignKey(Dog, related_name="related_dog", null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	closed = models.BooleanField()


class Message(models.Model):
	thread = models.ForeignKey(MessageThread)
	sender = models.ForeignKey(Person,related_name="sender")
	content = models.TextField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
	dog = models.ForeignKey(Dog, related_name="dog",verbose_name='Cão')
	adopter = models.ForeignKey(Person,related_name="adopter", null=True, blank=True,verbose_name='Adotador')
	giver = models.ForeignKey(Person,related_name="giver", null=True, blank=True,verbose_name='Doador')
	title = models.TextField(max_length=50,verbose_name='Título')
	content = models.TextField(max_length=500,verbose_name='Sua história')
	date = models.DateTimeField(auto_now_add=True,verbose_name='Data')

class MessageForm(ModelForm):

	class Meta:
		model = Message
		exclude = ['thread', 'sender', 'date']

class PersonForm(ModelForm):
	def clean_password(self):
		print 'testing'


	class Meta:
		model = Person
		exclude = ['address', 'user','answers']

class DogForm(ModelForm):

	def clean_birth_date(self):
		date = self.cleaned_data['birth_date']

		if date is not None and date > datetime.date.today():
			raise ValidationError("A data de nascimento não pode ser no futuro")
		return date

	def clean_abandoned(self):
		return self.cleaned_data['abandoned'] == 'y'

	class Meta:
		model = Dog
		#photo = models.ImageField(upload_to = 'dog_images/', default = 'dog_images/None/no-img.jpg')
		exclude = ['address', 'adopted', 'adopted_by', 'in_adoption_by', 'in_adoption_process','characteristics']



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

class TestimonialForm(ModelForm):

	class Meta:
		model = Testimonial
		exclude = ['adopter','giver']

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
