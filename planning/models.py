from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
import random
#import base de donnée externe
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

couleur_rdm_list = (('#5578eb','#5578eb'),('#1dc9b7','#1dc9b7'),('#ff0000','#ff0000'),('#ff8f00','#ff8f00'),('#ffed00','#ffed00'))

class Theme(models.Model):
	nom = models.CharField(default="N-A",max_length=50)

	class Meta:
		verbose_name = "Theme"
		ordering = ['nom']

	def __str__(self):
		return self.nom

class Client(models.Model):
	nom = models.CharField(default="N-A",max_length=100)
	code_couleur = models.CharField(blank=True,max_length=30)
	date_joined = models.DateTimeField(default=timezone.now)
	avatar = models.ImageField(upload_to='avatar',default='avatar/default.png')
	email = models.CharField(default="N-A",max_length=100)
	telephone = models.CharField(default="N-A",max_length=100)
	site_web = models.CharField(default="N-A",max_length=100)
	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Client"
		ordering = ['id']

	def __str__(self):
		return self.nom

class Mission_type_client(models.Model):
	nom = models.CharField(default="N-A",max_length=50)
	theme = models.ManyToManyField(Theme,blank=True)
	client = models.ForeignKey(Client,blank=True,null=True,on_delete=models.CASCADE)
	favori = models.BooleanField(default=False)
	date_upload = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "Mission type"
		ordering = ['id']

	def __str__(self):
		return self.nom

class Adresse_client(models.Model):
	nom = models.CharField(default="N-A",max_length=50)
	adresse = models.CharField(default="N-A",max_length=100)
	ville = models.CharField(default="N-A",max_length=100)
	code_postal = models.CharField(default="N-A",max_length=10)
	client = models.ForeignKey(Client,blank=True,null=True,on_delete=models.CASCADE)
	favori = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Adresse"
		ordering = ['id']

	def __str__(self):
		return self.nom

class Piece_jointe_client(models.Model):
	nom = models.CharField(default="N-A",max_length=50)
	document =  models.FileField(upload_to='piece_jointe_client/',blank=True)
	date_upload = models.DateField(auto_now_add=True)
	favori = models.BooleanField(default=False)
	client = models.ForeignKey(Client,blank=True,null=True,on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Piece jointe"
		ordering = ['id']

	def __str__(self):
		return self.nom

class Profile_user(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	diminutif = models.CharField(default="N-A",max_length=10)
	telephone = models.CharField(default="N-A",max_length=20)
	ville = models.CharField(default="N-A",max_length=100)
	code_postal =  models.CharField(default="N-A",max_length=20)
	adresse = models.CharField(default="N-A",max_length=100)
	avatar = models.ImageField(upload_to='avatar',null=True,blank=True)
	archive = models.BooleanField(default=False)
	dernier_message = models.DateTimeField(blank=True,null=True)
	couleur_rdm = models.CharField(choices=couleur_rdm_list,blank=True,max_length=20)

	class Meta:
		verbose_name = "Profile"
		ordering = ['id']

	def __str__(self):
		return (self.user.first_name + " " + self.user.last_name)


class Competence(models.Model):
	nom = models.ForeignKey(Theme,blank=True,null=True,on_delete=models.CASCADE)
	consultant = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
	note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
	date_modification = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "Competence"
		ordering = ['nom']

	def __str__(self):
		return self.nom.nom

class bdd_messages(models.Model):
	user = models.ForeignKey(User, related_name='user',blank=True,null=True)
	consultant = models.ForeignKey(User, related_name='consultant',blank=True,null=True)
	message = models.TextField()
	date = models.DateTimeField(default=timezone.now, verbose_name="Date d'envoi")
	lu = models.BooleanField(default = False)
	
	class Meta:
		verbose_name = "Message"
		ordering = ['date']
	
	def __str__(self):
		return self.message


class Statut_contrat(models.Model):
	nom = models.CharField(default="N-A",max_length=100)
	code_couleur = models.CharField(blank=True,max_length=30)

	class Meta:
		verbose_name = "Contrat statut"
		ordering = ['nom']

	def __str__(self):
		return self.nom

class Statut_mission(models.Model):
	nom = models.CharField(default="N-A",max_length=100)
	code_couleur = models.CharField(blank=True,max_length=30)

	class Meta:
		verbose_name = "Mission statut"
		ordering = ['nom']
		
	def __str__(self):
		return self.nom

class Statut_journee(models.Model):
	nom = models.CharField(default="N-A",max_length=100)
	code_couleur = models.CharField(blank=True,max_length=30)

	class Meta:
		verbose_name = "Journée statut"
		ordering = ['nom']
		
	def __str__(self):
		return self.nom


class Jour_semaine(models.Model):
	nom = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Jours semaine"
		ordering = ['nom']
		
	def __str__(self):
		return self.nom

class Jour_bloque(models.Model):
	nom_bdd = 'Jour_bloque'

	jour_semaine = models.ManyToManyField(Jour_semaine,blank=True)
	
	class Meta:
		verbose_name = "Jours bloqué"
		
	def __str__(self):
		return self.nom_bdd


class Jour_annee_bloque(models.Model):
	nom_bdd = 'Jour_annee_bloque'

	date = models.DateField(auto_now = False, auto_now_add = False,blank=True)
	est_recurrent = models.BooleanField(default = False)

	client = models.ForeignKey(Jour_bloque,blank=True,null=True,on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Jours année bloqué"
		ordering = ['date']
		
	def __str__(self):
		return self.nom_bdd


class Contrat(models.Model):
	nom = models.CharField(default="N-A",max_length=100)
	date_debut = models.DateField(auto_now = False, auto_now_add = False)
	date_fin = models.DateField(auto_now = False, auto_now_add = False)
	client = models.ForeignKey(Client,blank=True,null=True,on_delete=models.CASCADE)
	statut = models.ForeignKey(Statut_contrat,blank=True,null=True,on_delete=models.SET_NULL)

	class Meta:
		verbose_name = "Contrat"
		ordering = ['nom']
		
	def __str__(self):
		return self.nom

class Mission(models.Model):
	nom_bdd = 'Mission'

	jour_de_mission = models.DateField(auto_now = False, auto_now_add = False,blank=True)
	heure_debut = models.TimeField(auto_now=False, auto_now_add=False)
	heure_fin = models.TimeField(auto_now=False, auto_now_add=False)

	adresse = models.ForeignKey(Adresse_client,blank=True,null=True,on_delete=models.SET_NULL)
	statut = models.ForeignKey(Statut_mission,blank=True,null=True,on_delete=models.SET_NULL)
	utilisateur = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
	contrat = models.ForeignKey(Contrat,blank=True,null=True,on_delete=models.CASCADE)

	mission_type = models.ForeignKey(Mission_type_client,blank=True,null=True,on_delete=models.SET_NULL)

	document = models.ManyToManyField(Piece_jointe_client,related_name='piece_jointe',blank=True)

	class Meta:
		verbose_name = "Missions jour"
		ordering = ['jour_de_mission']

	def __str__(self):
		return self.nom_bdd

class Document_supplementaire(models.Model):
	nom = models.CharField(default="N-A",max_length=50)
	document =  models.FileField(upload_to='piece_jointe_supplementaire/',blank=True)
	date_upload = models.DateField(auto_now_add=True)
	mission = models.ForeignKey(Mission,blank=True,null=True,on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Documents supplémentaire"
		ordering = ['id']

	def __str__(self):
		return self.nom

class Document_rendu(models.Model):
	nom = models.CharField(default="N-A",max_length=50)
	document =  models.FileField(upload_to='piece_jointe_rendu/',blank=True)
	date_upload = models.DateField(auto_now_add=True)
	mission = models.ForeignKey(Mission,blank=True,null=True,on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Documents rendu"
		ordering = ['id']

	def __str__(self):
		return self.nom