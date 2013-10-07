from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField('data de nascimento aproximada')
    SIZE_CHOICES = ("Pequeno", "Médio", "Grande") #complementar
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    description = models.TextField() 
    SEX_CHOICES = ("Macho","Fêmea")
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    color = models.CharField()
    breed = models.ForeignKey(Breed)
    #A ideia é que um cachorro seja associado a um endereço da pessoa, e não à pessoa. Se quiser ser associada a ela, é só
    #colocar que o endereço do cachorro é o mesmo que o dela, e eles vão ficar sincronizados
    address = models.ForeignKey(Address)
    adopted = models.BooleanField()



class Breed(models.Model):
	#aqui precisa ser limitado

class Address(models.Model):
	#precisa ter telefone de contato também
	street = models.CharField()
	number = models.CharField()
	apartment = models.CharField()
	neighbourhood = models.CharField()
	city = models.CharField()
	STATE_CHOICES = (
		("Acre", "AC"),
		("Alagoas", "AL"),
		("Amapá", "AP"),
		("Amazonas", "AM"),
		("Bahia" ", BA"),
		("Ceará", "CE"),
		("Distrito Federal", "DF"),
		("Espírito Santo", "ES"),
		("Goiás", "GO"),
		("Maranhão", "MA"),
		("Mato Grosso", "MT"),
		("Mato Grosso do Sul", "MS"),
		("Minas Gerais", "MG"),
		("Pará", "PA"),
		("Paraíba", "PB"),
		("Paraná", "PR"),
		("Pernambuco", "PE"),
		("Piauí", "PI"),
		("Rio de Janeiro", "RJ"),
		("Rio Grande do Norte", "RN"),
		("Rio Grande do Sul", "RS"),
		("Rondônia", "RO"),
		("Roraima", "RR"),
		("Santa Catarina", "SC"),
		("São Paulo", "SP"),
		("Sergipe", "SE"),
		("Tocantins", "TO"))
	state = models.CharField(max_length=2, choices=STATE_CHOICES)
	postal_code = models.CharField(max_length=9) #colocar validação


class Characteristic(models.Model):
	#aqui também precisa ser limitado, são características "imposed" perguntadas

#class Album(models.Model): #many photos and videos

#class Photo(models.Model):

#class Video(models.Model):

class Person(models.Model):
	user = models.OneToOneField(User)
	dogs_adopted = models.ManyToManyField(Dog) #Será o melhor jeito de fazer? pensei que só o
	#campo adopted seria o suficiente, mas aí não dá pra trackear quem colocou o cão pra adoção
	#depois de alguém ter adotado
	#o nome também não serve bem se o cara consegue cadastrar seus próprios cães, mas acho que serve
	dogs_to_adoption = models.ManyToManyField(Dog) 
	birth_date = models.DateField()
	SEX_CHOICES = ("Masculino","Feminino")
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    answers = models.OneToOneField(Answer)


class Answers(models.Model):
	#conjunto de true/none/false também
