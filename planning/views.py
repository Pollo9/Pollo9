from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound,Http404, JsonResponse
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.contrib.auth.models import Group,User,Permission
import random
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.paginator import Paginator
import datetime
import locale
locale.setlocale(locale.LC_TIME,'')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic.edit import FormMixin

from django.views.generic import DetailView, ListView

# Create your views here.
from .models import *
from .forms import *

#ajax/json
from django.http import HttpResponse
from django import http
from django.core import serializers
import json

from django.db.models import Max
import os

from django.contrib.admin.models import LogEntry
from django.contrib.admin.utils import unquote

def get_content_type_for_model(obj): # Since this module gets imported in the application's root package, # it cannot import models from other applications at the module level.
	from django.contrib.contenttypes.models import ContentType
	return ContentType.objects.get_for_model(obj, for_concrete_model=False)

couleur_rdm_list = ('#5578eb','#1dc9b7','#ff0000','#ff8f00','#ffed00')

today = datetime.today()
mois = date(today.year,today.month,1)
N = today.weekday()
past = datetime.now() - timedelta(days=N)

@login_required
def erreur_403(request):
	context = locals()
	template = 'permission.html'
	return render(request,template,context)

@login_required
def reglages(request):
	context = locals()
	template = 'reglages.html'
	return render(request,template,context)

@login_required
def reglage_statut_missions(request):

	missions = Statut_mission.objects.all()

	response_data = {}

	if (request.POST.get('action') == 'ajouter_mission'):
		nom = request.POST.get("nom_mission")
		couleur = request.POST.get("couleur_mission")
		missions_creer = Statut_mission.objects.create(nom=nom,code_couleur=couleur)		

		response_data['nom'] = nom
		response_data['couleur'] = couleur
		response_data['id'] = missions_creer.id


		return JsonResponse(response_data)

	if (request.POST.get('action') == 'edit_mission'):
		id_mission = request.POST.get("id_mission")
		le_missions = Statut_mission.objects.get(id=id_mission)
		nom = le_missions.nom
		couleur = le_missions.code_couleur
		if couleur == '':
			couleur = "#0c7ff1"

		response_data['nom'] = nom
		response_data['couleur'] = couleur

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'supprimer_mission'):
		id_missions = request.POST.get("id_mission")
		Statut_mission.objects.get(id=id_missions).delete()

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'modifier_mission'):
		id_missions = request.POST.get("id_mission")
		nom = request.POST.get("nom_mission")
		couleur = request.POST.get("couleur_mission")
		modif_mission = Statut_mission.objects.get(id=id_missions)
		modif_mission.nom = nom
		modif_mission.code_couleur = couleur
		modif_mission.save()

		response_data['nom'] = nom
		response_data['couleur'] = couleur
		response_data['id'] = modif_mission.id


		return JsonResponse(response_data)

	context = locals()
	template = 'reglages_app/reglage_statut_missions.html'
	return render(request,template,context)

@login_required
def reglage_statut_jours(request):

	jours = Statut_journee.objects.all()

	response_data = {}

	if (request.POST.get('action') == 'ajouter_jour'):
		nom = request.POST.get("nom_jour")
		couleur = request.POST.get("couleur_jour")
		jours_creer = Statut_journee.objects.create(nom=nom,code_couleur=couleur)		

		response_data['nom'] = nom
		response_data['couleur'] = couleur
		response_data['id'] = jours_creer.id


		return JsonResponse(response_data)

	if (request.POST.get('action') == 'edit_jour'):
		id_jour = request.POST.get("id_jour")
		le_jours = Statut_journee.objects.get(id=id_jour)
		nom = le_jours.nom
		couleur = le_jours.code_couleur
		if couleur == '':
			couleur = "#0c7ff1"

		response_data['nom'] = nom
		response_data['couleur'] = couleur

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'supprimer_jour'):
		id_jours = request.POST.get("id_jour")
		Statut_journee.objects.get(id=id_jours).delete()

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'modifier_jour'):
		id_jours = request.POST.get("id_jour")
		nom = request.POST.get("nom_jour")
		couleur = request.POST.get("couleur_jour")
		modif_jour = Statut_journee.objects.get(id=id_jours)
		modif_jour.nom = nom
		modif_jour.code_couleur = couleur
		modif_jour.save()

		response_data['nom'] = nom
		response_data['couleur'] = couleur
		response_data['id'] = modif_jour.id


		return JsonResponse(response_data)

	context = locals()
	template = 'reglages_app/reglage_statut_jours.html'
	return render(request,template,context)

@login_required
def reglage_statut_contrats(request):

	contrats = Statut_contrat.objects.all()

	response_data = {}

	if (request.POST.get('action') == 'ajouter_contrat'):
		nom = request.POST.get("nom_contrat")
		couleur = request.POST.get("couleur_contrat")
		contrats_creer = Statut_contrat.objects.create(nom=nom,code_couleur=couleur)		

		response_data['nom'] = nom
		response_data['couleur'] = couleur
		response_data['id'] = contrats_creer.id


		return JsonResponse(response_data)

	if (request.POST.get('action') == 'edit_contrat'):
		id_contrat = request.POST.get("id_contrat")
		le_contrats = Statut_contrat.objects.get(id=id_contrat)
		nom = le_contrats.nom
		couleur = le_contrats.code_couleur
		if couleur == '':
			couleur = "#0c7ff1"

		response_data['nom'] = nom
		response_data['couleur'] = couleur

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'supprimer_contrat'):
		id_contrats = request.POST.get("id_contrat")
		Statut_contrat.objects.get(id=id_contrats).delete()

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'modifier_contrat'):
		id_contrats = request.POST.get("id_contrat")
		nom = request.POST.get("nom_contrat")
		couleur = request.POST.get("couleur_contrat")
		modif_contrat = Statut_contrat.objects.get(id=id_contrats)
		modif_contrat.nom = nom
		modif_contrat.code_couleur = couleur
		modif_contrat.save()

		response_data['nom'] = nom
		response_data['couleur'] = couleur
		response_data['id'] = modif_contrat.id


		return JsonResponse(response_data)

	context = locals()
	template = 'reglages_app/reglage_statut_contrats.html'
	return render(request,template,context)

@login_required
def reglage_groupes(request):

	perms = Permission.objects.all()
	groupes = Group.objects.all()
	response_data = {}

	if (request.POST.get('action') == 'ajouter_groupe'):
		print("add")
		list_perm = request.POST.getlist("select_permissions[]")
		nom = request.POST.get("nom_groupe")
		groupe_creer, created = Group.objects.get_or_create(name=nom)
		list_permission = []
		for ob in list_perm:
			permission = Permission.objects.get(id=ob)
			groupe_creer.permissions.add(permission)
			list_permission.append(permission.name)


		response_data['list_perm'] = list_permission
		response_data['nom'] = nom
		response_data['id'] = groupe_creer.id


		return JsonResponse(response_data)

	if (request.POST.get('action') == 'edit_groupe'):
		print("edit_goupe")
		id_groupe = request.POST.get("id_groupe")
		print(id_groupe)
		le_groupe = Group.objects.get(id=id_groupe)
		nom = le_groupe.name
		list_permission_name = []
		list_permission_id = []
		for perm in le_groupe.permissions.all():
			list_permission_name.append(perm.name)
			list_permission_id.append(perm.id)

		response_data['list_perm_name'] = list_permission_name
		response_data['list_perm_id'] = list_permission_id
		response_data['nom'] = nom

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'supprimer_groupe'):
		print("supp")
		id_groupe = request.POST.get("id_groupe")
		Group.objects.get(id=id_groupe).delete()

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'modifier_groupe'):
		print("modifier_groupe")
		id_groupe = request.POST.get("id_groupe")
		nom = request.POST.get("nom_groupe")
		list_perm = request.POST.getlist("select_permissions[]")
		modif_group = Group.objects.get(id=id_groupe)
		modif_group.name = nom
		modif_group.save()
		modif_group.permissions.clear()
		list_permission = []
		for ob in list_perm:
			permission = Permission.objects.get(id=ob)
			modif_group.permissions.add(permission)
			list_permission.append(permission.name)


		response_data['list_perm'] = list_permission
		response_data['nom'] = nom


		return JsonResponse(response_data)


	context = locals()
	template = 'reglages_app/groupes.html'
	return render(request,template,context)

@login_required
def reglage_themes(request):

	themes = Theme.objects.all()

	response_data = {}

	if (request.POST.get('action') == 'ajouter_theme'):
		nom = request.POST.get("nom_theme")
		themes_creer = Theme.objects.create(nom=nom)		

		response_data['nom'] = nom
		response_data['id'] = themes_creer.id


		return JsonResponse(response_data)

	if (request.POST.get('action') == 'edit_theme'):
		id_theme = request.POST.get("id_theme")
		print(id_theme)
		le_themes = Theme.objects.get(id=id_theme)
		nom = le_themes.nom

		response_data['nom'] = nom

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'supprimer_theme'):
		id_themes = request.POST.get("id_theme")
		Theme.objects.get(id=id_themes).delete()

		return JsonResponse(response_data)

	if (request.POST.get('action') == 'modifier_theme'):
		id_themes = request.POST.get("id_theme")
		nom = request.POST.get("nom_theme")
		modif_theme = Theme.objects.get(id=id_themes)
		modif_theme.nom = nom
		modif_theme.save()

		response_data['nom'] = nom
		response_data['id'] = modif_theme.id


		return JsonResponse(response_data)

	context = locals()
	template = 'reglages_app/themes.html'
	return render(request,template,context)

@login_required
def index (request):

	if request.user.groups.filter(name__in=['Consultant']).exists():
		return HttpResponseRedirect('/planning/')
	elif request.user.groups.filter(name__in=['Administrateur']).exists():
		return HttpResponseRedirect('/planning/')
	else:
		return HttpResponseRedirect('/permission/')

def generate_mdp():
	caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789?!@%}{[]"
	longueur = 10
	mdp = ""
	compteur = 0
	first_letter = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
	mdp += first_letter[random.randint(0, len(first_letter)-1)]
	while compteur < longueur-1:
		lettre = caracteres[random.randint(0, len(caracteres)-1)] #On tire au hasard une lettre
		mdp += lettre #On ajoute la lettre au mot de passe
		compteur += 1 #On incrémente le compteur de lettres

	return mdp

#### Partie administrateur
@login_required
def planning(request):
	context = locals()
	template = 'planning.html'
	return render(request,template,context)

@permission_required('auth.view_user', raise_exception=True)
@login_required
def utilisateurs(request):

	response_data = {}
	if (request.POST.get('action') == 'ajouter_utilisateur'):

		nom_utilisateur = request.POST.get('nom_utilisateur')
		prenom_utilisateur = request.POST.get('prenom_utilisateur')
		email_utilisateur = request.POST.get('email_utilisateur')
		telephone_utilisateur = request.POST.get('telephone_utilisateur')
		group_selec = request.POST.getlist("select_group_ajout_utilisateur[]")
		envoi_mail = (request.POST.get("envoi_mail_ajout_utilisateur") == "true")

		mdp = generate_mdp()

		user = User.objects.create_user(username=email_utilisateur,email=email_utilisateur,password=mdp)
		user.first_name = prenom_utilisateur
		user.last_name = nom_utilisateur
		user.save()
		all_group = []
		for i in group_selec:
			group = Group.objects.get(name=i)
			user.groups.add(group)
			all_group.append(i)
		user.save()
		profile_user = Profile_user.objects.create(user=user)
		profile_user.diminutif = prenom_utilisateur[0] + " " + nom_utilisateur[0]
		profile_user.telephone = telephone_utilisateur

		ma_couleur = couleur_rdm_list[random.randint(0, len(couleur_rdm_list)-1)]
		profile_user.couleur_rdm = ma_couleur;
		profile_user.save()

		if envoi_mail:
			print('ENVOIE MAIL')


		response_data['group_utilisateur'] = all_group
		response_data['nom_utilisateur'] = nom_utilisateur
		response_data['prenom_utilisateur'] = prenom_utilisateur
		response_data['email_utilisateur'] = email_utilisateur
		response_data['telephone_utilisateur'] = telephone_utilisateur
		response_data['id_utilisateur'] = user.id
		response_data['date_joined_utilisateur'] = user.date_joined
		response_data['is_active'] = user.is_active
		response_data['diminutif_utilisateur'] = user.profile.diminutif
		response_data['couleur_rdm_utilisateur'] = user.profile.couleur_rdm

		return JsonResponse(response_data)

	if (request.POST.get("action") == "supprimer_utilisateur"):
		to_delete = User.objects.get(id=request.POST.get("id"))
		response_data['id_utilisateur'] = to_delete.id
		to_delete.delete()
		return JsonResponse(response_data)
		
	if (request.POST.get("action") == 'supprimer_element_select') :
		utilisateur_selectionne = request.POST.getlist('utilisateur_selectionne[]')
		for ob in utilisateur_selectionne:
			rem = User.objects.get(id=ob)
			rem.delete()
			print(ob)
		message = 'Supprimer'
		return JsonResponse(response_data)

	if request.POST.get('action') == 'mettre_a_jour_status_active':
		utilisateur_selectionner = request.POST.getlist('utilisateur_selectionne[]')
		for ob in utilisateur_selectionner:
			rem = User.objects.get(id=ob)
			rem.is_active = True
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)

	if request.POST.get('action') == 'mettre_a_jour_status_inactive':
		utilisateur_selectionner = request.POST.getlist('utilisateur_selectionne[]')
		for ob in utilisateur_selectionner:
			rem = User.objects.get(id=ob)
			rem.is_active = False
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)

	utilisateurs = User.objects.all()
	groupes = Group.objects.all()

	context = locals()
	template = 'utilisateurs.html'
	return render(request,template,context)

@permission_required('auth.view_user_profile', raise_exception=True)
@login_required
def profil_utilisateur(request,datapk):

	utilisateur = User.objects.get(id=datapk)
	themes = Theme.objects.all()
	list_competence = utilisateur.competence_set.all().order_by("-note")

	for i in list_competence:
		if (i.nom in themes):
			themes = themes.exclude(nom=i.nom.nom)

	response_data = {}

	if (request.POST.get('action') == "supprimer_competence"):
		the_competence = utilisateur.competence_set.get(id=request.POST.get('id_competence'))
		
		response_data['id_competence'] = the_competence.id
		the_theme = Theme.objects.get(nom=the_competence.nom)
		response_data['id_theme'] = the_theme.id
		response_data['nom_theme'] = the_theme.nom
		response_data['message'] = "La competence a bien été retirée."
		the_competence.delete()

		return JsonResponse(response_data)


	if (request.POST.get('action') == "edit_competence"):
		edit_note_competence = request.POST.get('edit_note_competence')
		edit_id_competence = int(request.POST.get('edit_id_competence'))

		competence = Competence.objects.get(id=edit_id_competence)
		competence.note = edit_note_competence
		competence.save()

		response_data['edit_id_competence'] = edit_id_competence
		response_data['edit_note_competence'] = edit_note_competence
		response_data["message"] = "La compétence a bien été modifiée."

		return JsonResponse(response_data)


	if (request.POST.get("action") == "ajouter_competence"):
		comp = Competence.objects.create(nom = Theme.objects.get(id=request.POST.get("nom_competence")),consultant=utilisateur,note=request.POST.get("note_competence"))
		comp.save()
		response_data['id_competence'] = comp.id
		response_data['nom_competence'] = comp.nom.nom
		response_data['note_competence'] = comp.note
		response_data['date_competence'] = comp.date_modification.strftime("%d %B %Y")
		response_data["message"] = "La compétence a bien été ajoutée."
		response_data["id_theme"] = comp.nom.id

		return JsonResponse(response_data)

	if (request.POST.get("action") == "editer_utilisateur"):
		form = ProfileForm(request.POST, request.FILES,instance=utilisateur.profile)
		if form.is_valid():
			profile_for_avatar = form.save(commit=False)
			profile_for_avatar.save()

		profile_utilisateur = utilisateur.profile
		utilisateur.first_name = request.POST.get("utilisateur_prenom")
		utilisateur.last_name = request.POST.get("utilisateur_nom")
		profile_utilisateur.diminutif = request.POST.get("utilisateur_diminutif")
		profile_utilisateur.telephone = request.POST.get("utilisateur_telephone")
		utilisateur.email = request.POST.get("utilisateur_email")
		profile_utilisateur.ville = request.POST.get("utilisateur_ville")
		profile_utilisateur.code_postal = request.POST.get("utilisateur_code_postal")
		profile_utilisateur.adresse = request.POST.get("utilisateur_adresse")
		utilisateur.is_active = (request.POST.get("utilisateur_activer") == "true")

		profile_utilisateur.save()
		utilisateur.save()

		response_data['utilisateur_prenom'] = utilisateur.first_name
		response_data['utilisateur_nom'] = utilisateur.last_name
		response_data['utilisateur_diminutif'] = profile_utilisateur.diminutif
		response_data['utilisateur_telephone'] = profile_utilisateur.telephone
		response_data['utilisateur_email'] = utilisateur.email
		response_data['utilisateur_activer'] = utilisateur.is_active
		response_data['utilisateur_ville'] = profile_utilisateur.ville
		response_data['utilisateur_code_postal'] = profile_utilisateur.code_postal
		response_data['utilisateur_adresse'] = profile_utilisateur.adresse
		try:
			response_data['avatar_utilisateur'] = profile_utilisateur.avatar.url
		except:
			response_data['avatar_utilisateur'] = ""
		response_data['message'] = "L'utilisateur a bien été modifié."

		return JsonResponse(response_data)
	
	else:
		form = ProfileForm(instance=utilisateur.profile)


	context = locals()
	template = 'profil_utilisateur.html'
	return render(request,template,context)

@permission_required('planning.view_client', raise_exception=True)
@login_required
def client(request):


	response_data = {}
	if (request.POST.get('action') == 'ajouter_client'):

		nom_client = request.POST.get('nom_client')
		couleur_client = request.POST.get('couleur_client')
		actif_client = request.POST.get('actif_client')

		client = Client.objects.create(nom=nom_client,code_couleur=couleur_client)
		client.archive = not (actif_client == "true")
		client.save()

		response_data['nom_client'] = nom_client
		response_data['couleur_client'] = couleur_client
		response_data['id_client'] = client.id
		response_data['date_joined_client'] = client.date_joined
		response_data['is_active'] = not client.archive
		response_data['avatar_client'] = client.avatar.url

		return JsonResponse(response_data)

	if (request.POST.get("action") == "supprimer_client"):
		to_delete = Client.objects.get(id=request.POST.get("id"))
		response_data['id_client'] = to_delete.id
		to_delete.delete()
		return JsonResponse(response_data)
		
	if (request.POST.get("action") == 'supprimer_element_select') :
		client_selectionne = request.POST.getlist('client_selectionne[]')
		for ob in client_selectionne:
			rem = Client.objects.get(id=ob)
			rem.delete()
		message = 'Supprimer'
		return JsonResponse(response_data)

	if request.POST.get('action') == 'mettre_a_jour_status_active':
		client_selectionne = request.POST.getlist('client_selectionne[]')
		for ob in client_selectionne:
			rem = Client.objects.get(id=ob)
			rem.archive = False
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)


	if request.POST.get('action') == 'mettre_a_jour_status_inactive':
		client_selectionne = request.POST.getlist('client_selectionne[]')
		for ob in client_selectionne:
			rem = Client.objects.get(id=ob)
			rem.archive = True
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)


	clients = Client.objects.all()

	context = locals()
	template = 'client.html'
	return render(request,template,context)

@permission_required('planning.view_client_profile', raise_exception=True)
@login_required
def profil_client(request,datapk):

	client = Client.objects.get(id=datapk)
	action_list = LogEntry.objects.filter( object_id=unquote(datapk), content_type=get_content_type_for_model(client) ).select_related().order_by('-action_time')
	response_data = {}
	themes = Theme.objects.all()

	if (request.POST.get("action") == "ajouter_adresse"):
		ajout_nom_adresse = request.POST.get('ajout_nom_adresse')
		ajout_adresse_adresse = request.POST.get('ajout_adresse_adresse')
		ajout_ville_adresse = request.POST.get('ajout_ville_adresse')
		ajout_code_postal_adresse = request.POST.get('ajout_code_postal_adresse')
		adresse = Adresse_client.objects.create(nom=ajout_nom_adresse,adresse=ajout_adresse_adresse,ville=ajout_ville_adresse,code_postal=ajout_code_postal_adresse,client=client)
		adresse.save()

		response_data['ajout_code_postal_adresse'] = ajout_code_postal_adresse
		response_data['ajout_nom_adresse'] = ajout_nom_adresse
		response_data['ajout_adresse_adresse'] = ajout_adresse_adresse
		response_data['ajout_ville_adresse'] = ajout_ville_adresse
		response_data["message"] = "La compétence a bien été ajoutée."
		response_data["ajout_id_adresse"] = int(adresse.id)

		return JsonResponse(response_data)

		response_data['id_adresse'] = adresse.id
		response_data['is_favori'] = adresse.favori

		return JsonResponse(response_data)	

	if (request.POST.get("action") == "add_reset_favori_adresse"):
		id_adresse = int(request.POST.get('id_adresse'))
		adresse = Adresse_client.objects.get(id=id_adresse)

		if (adresse.favori == True):
			adresse.favori = False
			response_data["message"] = "L'adresse a bien été retirée des favoris."
		else:
			adresse.favori = True
			response_data["message"] = "L'adresse a bien été ajoutée en favori."

		adresse.save()

		response_data['id_adresse'] = adresse.id
		response_data['is_favori'] = adresse.favori

		return JsonResponse(response_data)	

	if (request.POST.get("action") == "edit_adresse"):
		edit_nom_adresse = request.POST.get('edit_nom_adresse')
		edit_ville_adresse = request.POST.get('edit_ville_adresse')
		edit_adresse_adresse = request.POST.get('edit_adresse_adresse')
		edit_code_postal_adresse = request.POST.get('edit_code_postal_adresse')
		edit_id_adresse = int(request.POST.get('edit_id_adresse'))

		adresse = Adresse_client.objects.get(id=edit_id_adresse)
		adresse.nom = edit_nom_adresse
		adresse.ville = edit_ville_adresse
		adresse.adresse = edit_adresse_adresse
		adresse.code_postal = edit_code_postal_adresse
		adresse.save()

		response_data['edit_id_adresse'] = request.POST.get('edit_id_adresse')
		response_data['edit_nom_adresse'] = edit_nom_adresse
		response_data['edit_ville_adresse'] = edit_ville_adresse
		response_data['edit_adresse_adresse'] = edit_adresse_adresse
		response_data['edit_code_postal_adresse'] = edit_code_postal_adresse
		response_data["message"] = "L'adresse a bien été modifiée."

		return JsonResponse(response_data)	

	if (request.POST.get('action') == "supprimer_adresse"):
		the_adresse = client.adresse_client_set.get(id=request.POST.get('id_adresse'))
		
		response_data['id_adresse'] = the_adresse.id
		response_data['message'] = "L'adresse a bien été supprimée."

		the_adresse.delete()

		return JsonResponse(response_data)



	if (request.POST.get("action") == "edit_piece_jointe"):
		pj = Piece_jointe_client.objects.get(id=request.POST.get("edit_id_piece_jointe"))
		form_piece_jointe = ProfileClientPieceJointeForm(request.POST, request.FILES, instance=pj)
		if form_piece_jointe.is_valid():
			my_pj = form_piece_jointe.save(commit=False)
			my_pj.nom = request.POST.get("edit_nom_piece_jointe")
			my_pj.client = client
			my_pj.save()

			response_data['edit_id_piece_jointe'] = my_pj.id
			response_data['edit_nom_piece_jointe'] = my_pj.nom
			response_data['edit_document_piece_jointe'] = my_pj.document.url
			response_data['edit_date_upload_piece_jointe'] = my_pj.date_upload
			response_data['message'] = "La pièce jointe a bien été modifiée."

		return JsonResponse(response_data)	

	if (request.POST.get('action') == "supprimer_piece_jointe"):
		the_piece_jointe = client.piece_jointe_client_set.get(id=request.POST.get('id_piece_jointe'))
		
		response_data['id_piece_jointe'] = the_piece_jointe.id
		response_data['message'] = "La pièce jointe a bien été supprimée."

		the_piece_jointe.delete()

		return JsonResponse(response_data)

	if (request.POST.get("action") == "add_reset_favori_piece_jointe"):
		id_piece_jointe = int(request.POST.get('id_piece_jointe'))
		piece_jointe = Piece_jointe_client.objects.get(id=id_piece_jointe)

		if (piece_jointe.favori == True):
			piece_jointe.favori = False
			response_data["message"] = "La pièce jointe a bien été retirée des favoris."
		else:
			piece_jointe.favori = True
			response_data["message"] = "La pièce jointe a bien été ajoutée en favori."

		piece_jointe.save()

		response_data['id_piece_jointe'] = piece_jointe.id
		response_data['is_favori'] = piece_jointe.favori

		return JsonResponse(response_data)	

	if (request.POST.get("action") == "ajout_piece_jointe"):
		form_add = ProfileClientAddPieceJointeForm(request.POST, request.FILES)
		if form_add.is_valid():
			my_pj = form_add.save(commit=False)
			my_pj.nom = request.POST.get("ajout_nom_piece_jointe")
			my_pj.client = client
			my_pj.save()
		
		response_data['ajout_nom_piece_jointe'] = my_pj.nom
		response_data['ajout_piece_jointe_piece_jointe'] = my_pj.document.url
		response_data["message"] = "La pièce jointe a bien été ajoutée."
		response_data["ajout_id_piece_jointe"] = int(my_pj.id)
		response_data["ajout_date_upload_piece_jointe"] = my_pj.date_upload
		return JsonResponse(response_data)


	if (request.POST.get("action") == "ajouter_mission_type"):
		ajout_nom_mission_type = request.POST.get('ajout_nom_mission_type')
		theme_select = request.POST.getlist("select_mission_type_ajout[]")

		mission_type = Mission_type_client.objects.create(nom=ajout_nom_mission_type,client=client)
		mission_type.theme = theme_select
		mission_type.save()

		list_to_send = []
		for id_theme in theme_select:
			list_to_send.append(Theme.objects.get(id=id_theme).nom)

		response_data['ajout_nom_mission_type'] = ajout_nom_mission_type
		response_data['ajout_date_upload_mission_type'] = mission_type.date_upload
		response_data['theme_select'] = list_to_send
		response_data["message"] = "La mission type a bien été ajoutée."
		response_data["ajout_id_mission_type"] = int(mission_type.id)

		return JsonResponse(response_data)

		response_data['id_mission_type'] = mission_type.id
		response_data['is_favori'] = mission_type.favori

		return JsonResponse(response_data)	

	if (request.POST.get("action") == "add_reset_favori_mission_type"):
		id_mission_type = int(request.POST.get('id_mission_type'))
		mission_type = Mission_type_client.objects.get(id=id_mission_type)

		if (mission_type.favori == True):
			mission_type.favori = False
			response_data["message"] = "La mission type a bien été retirée des favoris."
		else:
			mission_type.favori = True
			response_data["message"] = "La mission type a bien été ajoutée en favori."

		mission_type.save()

		response_data['id_mission_type'] = mission_type.id
		response_data['is_favori'] = mission_type.favori

		return JsonResponse(response_data)	

	if (request.POST.get("action") == "edit_mission_type"):
		edit_nom_mission_type = request.POST.get('edit_nom_mission_type')
		theme_select = request.POST.getlist("theme_select[]")
		edit_id_mission_type = int(request.POST.get('edit_id_mission_type'))
		list_to_send = []
		mission_type = Mission_type_client.objects.get(id=edit_id_mission_type)
		mission_type.theme.remove()
		mission_type.theme = theme_select

		for id_theme in theme_select:
			list_to_send.append(Theme.objects.get(id=id_theme).nom)

		mission_type.nom = edit_nom_mission_type
		mission_type.save()

		response_data['edit_id_mission_type'] = request.POST.get('edit_id_mission_type')
		response_data['edit_nom_mission_type'] = edit_nom_mission_type
		response_data['edit_date_upload_mission_type'] = mission_type.date_upload
		response_data['theme_select'] = list_to_send
		response_data["message"] = "La mission type a bien été modifiée."

		return JsonResponse(response_data)	

	if (request.POST.get('action') == "supprimer_mission_type"):
		the_mission_type = client.mission_type_client_set.get(id=request.POST.get('id_mission_type'))
		
		response_data['id_mission_type'] = the_mission_type.id
		response_data['message'] = "La mission type a bien été supprimée."

		the_mission_type.delete()

		return JsonResponse(response_data)

	else:
		form_add = ProfileClientAddPieceJointeForm()


	if (request.POST.get("action") == "editer_client"):
		form = ProfileClientForm(request.POST, request.FILES,instance=client)
		if form.is_valid():
			profile_for_avatar = form.save(commit=False)
			profile_for_avatar.save()

		client.nom = request.POST.get("client_nom")
		client.email = request.POST.get("client_email")
		client.telephone = request.POST.get("client_telephone")
		client.site_web = request.POST.get("client_site_web")
		client.code_couleur = request.POST.get("client_couleur")
		client.archive = (not request.POST.get("client_activer") == "true")
		client.save()

		response_data['client_nom'] = client.nom
		response_data['client_email'] = client.email
		response_data['client_telephone'] = client.telephone
		response_data['client_site_web'] = client.site_web
		response_data['client_couleur'] = client.code_couleur
		response_data['client_activer'] = not client.archive
		response_data['avatar_consultant'] = client.avatar.url
		response_data['message'] = "Le client a bien été modifié."

		return JsonResponse(response_data)

	else:
		form = ProfileClientForm(instance=client)

	list_adresse_client = client.adresse_client_set.all().order_by("-favori")
	list_piece_jointe = client.piece_jointe_client_set.all().order_by("-favori")
	list_mission_type = client.mission_type_client_set.all().order_by("-favori")

	context = locals()
	template = 'profil_client.html'
	return render(request,template,context)

@login_required
def mission(request):

	response_data = {}
	if (request.POST.get('action') == 'ajouter_mission'):
		"""
		nom_client = request.POST.get('nom_client')
		couleur_client = request.POST.get('couleur_client')
		actif_client = request.POST.get('actif_client')

		client = Client.objects.create(nom=nom_client,code_couleur=couleur_client)
		client.archive = not (actif_client == "true")
		client.save()

		response_data['nom_client'] = nom_client
		response_data['couleur_client'] = couleur_client
		response_data['id_client'] = client.id
		response_data['date_joined_client'] = client.date_joined
		response_data['is_active'] = not client.archive
		response_data['avatar_client'] = client.avatar.url
		"""
		return JsonResponse(response_data)

	if (request.POST.get("action") == "supprimer_mission"):
		to_delete = Mission.objects.get(id=request.POST.get("id"))
		response_data['id_mission'] = to_delete.id
		to_delete.delete()
		return JsonResponse(response_data)
		
	if (request.POST.get("action") == 'supprimer_element_select') :
		mission_selectionnee = request.POST.getlist('mission_selectionnee[]')
		for ob in mission_selectionnee:
			rem = Mission.objects.get(id=ob)
			rem.delete()
			print(ob)
		message = 'Supprimer'
		return JsonResponse(response_data)

	if request.POST.get('action') == 'mettre_a_jour_status_attente':
		mission_selectionnee = request.POST.getlist('mission_selectionnee[]')
		statut = Statut_mission.objects.get(nom = "En attente")
		for ob in mission_selectionnee:
			rem = Mission.objects.get(id=ob)
			rem.statut = statut
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)

	if request.POST.get('action') == 'mettre_a_jour_status_en_cours':
		mission_selectionnee = request.POST.getlist('mission_selectionnee[]')
		statut = Statut_mission.objects.get(nom = "En cours")
		for ob in mission_selectionnee:
			rem = Mission.objects.get(id=ob)
			rem.statut = statut
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)

	if request.POST.get('action') == 'mettre_a_jour_status_historique':
		mission_selectionnee = request.POST.getlist('mission_selectionnee[]')
		statut = Statut_mission.objects.get(nom = "Historique")
		for ob in mission_selectionnee:
			rem = Mission.objects.get(id=ob)
			rem.statut = statut
			rem.save()
		message = 'Modifier'
		return JsonResponse(response_data)

	missions = Mission.objects.all()

	context = locals()
	template = 'mission.html'
	return render(request,template,context)

@login_required
def profil_mission(request,datapk):

	mission = Mission.objects.get(id=datapk)
	clients = Client.objects.all()
	consultants = User.objects.filter(groups__name__in=['Consultant'])
	adresses = Adresse_client.objects.all()
	types = Mission_type_client.objects.all()
	pieces_jointes = Piece_jointe_client.objects.all()
	statuts = Statut_mission.objects.all()
	response_data = {}

	if (request.POST.get("action") == "editer_mission"):

		mission.jour_de_mission = request.POST.get("mission_jour")
		mission.horaire_debut = request.POST.get("mission_debut")
		mission.horaire_fin = request.POST.get("mission_fin")
		mission.client = Client.objects.get(id = request.POST.get("mission_client"))
		mission.consultant = Profile_consultant.objects.get(id = request.POST.get("mission_consultant"))
		mission.statut = Statut_mission.objects.get(id = request.POST.get("mission_statut"))
		mission.adresse_de_mission = Adresse_client.objects.get(id = request.POST.get("mission_adresse"))
		mission.piece_jointe.clear()
		if request.POST.get("mission_pj[]"):
			mission.piece_jointe.add(Piece_jointe_client.objects.get(id = request.POST.get("mission_pj[]")))
		mission.mission_type = Mission_type_client.objects.get(id = request.POST.get("mission_type"))
		mission.is_client_visible = (request.POST.get("mission_client_visible") == "true")
		mission.is_adresse_visible = (request.POST.get("mission_adresse_visible") == "true")
		mission.piece_jointe_visible.clear()
		if request.POST.get("mission_pj_visible[]"):
			mission.piece_jointe_visible.add(Piece_jointe_client.objects.get(id = request.POST.get("mission_pj_visible[]")))
		mission.is_misson_type_visible = (request.POST.get("mission_type_visible") == "true")

		mission.save()

		response_data['client_url'] = '/administrateur/profil_client/'+str(mission.client.id)
		response_data['client_nom'] = mission.client.nom
		response_data['consultant_nom'] = mission.consultant.user.first_name+' '+mission.consultant.user.last_name
		response_data['consultant_url'] = '/administrateur/profil_consultant/'+str(mission.consultant.user.id)
		response_data['type_nom'] = mission.mission_type.nom
		
		response_data['mission_jour'] = str(mission.jour_de_mission)
		response_data['mission_debut'] = str(mission.horaire_debut)
		response_data['mission_fin'] = str(mission.horaire_fin)
		response_data['mission_client'] = mission.client.id
		response_data['mission_consultant'] = mission.consultant.id
		response_data['mission_statut'] = mission.statut.id
		response_data['mission_adresse'] = mission.adresse_de_mission.id
		response_data['mission_pj'] = []
		for pj in mission.piece_jointe.all():
			response_data['mission_pj'].append(pj.id)
		response_data['mission_type'] = mission.mission_type.id
		response_data['mission_client_visible'] = mission.is_client_visible
		response_data['mission_adresse_visible'] = mission.is_adresse_visible
		response_data['mission_pj_visible'] = []
		for pj in mission.piece_jointe_visible.all():
			response_data['mission_pj_visible'].append(pj.id)
		response_data['mission_type_visible'] = mission.is_misson_type_visible
		response_data['message'] = "La mission a bien été modifiée"

		return JsonResponse(response_data)

	context = locals()
	template = 'profil_mission.html'
	return render(request,template,context)

@login_required
def contrats(request):
	
	response_data={}

	if (request.POST.get("action") == 'supprimer_contrat'):
		to_del_contrat = Contrat.objects.get(id=request.POST.get('id'))
		response_data['id_contrat'] = to_del_contrat.id
		to_del_contrat.delete()

		return JsonResponse(response_data)

	if (request.POST.get("action")== "ajouter_contrat"):
		nom_contrat = request.POST.get("nom_contrat")
		client_contrat = Client.objects.get(id=request.POST.get("client_contrat"))
		date_debut_contrat = request.POST.get("date_debut_contrat")
		date_fin_contrat = request.POST.get("date_fin_contrat")
		statut_contrat = Statut_contrat.objects.get(id=request.POST.get("statut_contrat"))

		contrat = Contrat.objects.create(nom=nom_contrat,date_debut=date_debut_contrat,date_fin=date_fin_contrat,client=client_contrat,statut=statut_contrat)
		contrat.save()

		response_data['id_contrat'] = contrat.id
		response_data['nom_contrat'] = nom_contrat
		response_data['avatar_client'] = client_contrat.avatar.url
		response_data['nom_client'] = client_contrat.nom
		response_data['id_client'] = client_contrat.id
		response_data['date_debut_contrat'] = date_debut_contrat
		response_data['date_fin_contrat'] = date_fin_contrat
		response_data['statut_contrat'] = statut_contrat.nom
		response_data['code_couleur_statut_contrat'] = statut_contrat.code_couleur

		return JsonResponse(response_data)

	if (request.POST.get("action") == "supprimer_element_select"):
		liste_contrat = request.POST.getlist('contrat_selectionne[]')
		for id_contrat in liste_contrat:
			rem = Contrat.objects.get(id=id_contrat)
			rem.delete()
		message = 'Supprimer'
		return JsonResponse(response_data)

	if (request.POST.get("action") == "mettre_a_jour_status"):
		liste_contrat = request.POST.getlist('contrat_selectionne[]')
		for id_contrat in liste_contrat:
			to_change = Contrat.objects.get(id=id_contrat)
			to_change.statut = Statut_contrat.objects.get(id=request.POST.get("id_statut"))
			to_change.save()
		
		response_data["id_statut"] = to_change.statut.id
		response_data["nom_statut"] = to_change.statut.nom
		response_data["code_couleur_statut"] = to_change.statut.code_couleur

		message = 'Modifier'
		return JsonResponse(response_data)

	liste_client = Client.objects.filter(archive=False)
	liste_statut = Statut_contrat.objects.all()
	liste_contrat = Contrat.objects.all()
	context = locals()
	template = 'contrats.html'
	return render(request,template,context)

def mission_consultant(request):

	missions = Mission.objects.filter(consultant = request.user.profile)

	context = locals()
	template = 'consultant/mission.html'
	return render(request,template,context)
# grossebdd.petitebdd_set.all()
# var = get_object_or_404(Bdd, pk=id)

# MESSAGERIE
@login_required
def messagerie_administrateur(request):

	if not(request.user.groups.filter(name__in=['Administrateur']).exists()):
		return HttpResponseRedirect('/permission/')

	consultants_liste = User.objects.filter(groups__name__in=['Consultant']).order_by('-profile__dernier_message','last_name')
	paginator = Paginator(consultants_liste, 20)
	consultants = []
	response_data = {}

	for i in paginator.page_range:
		consultants.append(paginator.page(i))

	notif = {}
	for c in consultants_liste:
		msg = bdd_messages.objects.filter(user__username = c.username)
		compteur = 0
		for m in msg:
			if not m.lu:
				compteur += 1
		notif[c.id] = compteur

	msg = None
	consultant_selectionne = None

	context = locals()
	template = 'messagerie_administrateur.html'
	return render(request,template,context)

@login_required
def messagerie_consultant(request):
	
	if request.user.groups.filter(name__in=['Administrateur']).exists():
		return HttpResponseRedirect('administrateur/messagerie_administrateur/')
	elif not request.user.groups.filter(name__in=['Consultant']).exists():
		return HttpResponseRedirect('/permission/')

	response_data = {}
	if request.POST.get('action') == 'post':
		if request.POST.get('message') != '':
			contenu = request.POST.get('message')

			response_data['message'] = contenu
			response_data['date'] = timezone.localtime().strftime('%e %B %Y %H:%M')

			bdd_messages.objects.create(
				user = request.user,
				consultant = request.user,
				message = contenu,
			)
			p = Profile_consultant.objects.get(user = request.user)
			p.dernier_message = timezone.localtime()
			p.save()

			response_data['utilisateur'] = request.user

			return JsonResponse(response_data)

	msg = bdd_messages.objects.filter(consultant__username = request.user.username)

	for m in msg:
		if m.user.username != request.user.username:
			m.lu = True
			m.save()

	context = locals()
	template = 'consultant/messagerie_consultant.html'
	return render(request,template,context)

"""
@twilio_view
def sms(request):
	m = bdd_messages()
	e = User.objects.get(user_django__telephone = request.POST.get('From'))
	
	m.message = request.POST.get('Body','')
	m.user = e
	m.consultant = e
	m.save()
"""

# AJAX
def edit_competence_modal(request):

	competence_id = request.GET.get('id_competence')
	competence = Competence.objects.get(id=competence_id)

	context = locals()
	template = 'loadAjax/edit_competence_modal.html'
	return render(request,template,context)

def messagerie_administrateur_modal(request):

	if request.GET.get('id_consultant'):
		consultant_selectionne = User.objects.get(id = request.GET.get('id_consultant'))
	elif request.POST.get('id_consultant'):
		consultant_selectionne = User.objects.get(id = request.POST.get('id_consultant'))
	msg = bdd_messages.objects.filter(consultant = consultant_selectionne)
	response_data = {}

	if request.POST.get('action') == 'post':
		if request.POST.get('message') != '':
			contenu = request.POST.get('message')

			if (request.POST.get("message_sms") == "true"):
				print('sms')
				"""
				account_sid = settings.TWILIO_ACCOUNT_SID
				auth_token = settings.TWILIO_AUTH_TOKEN
				client = Client(account_sid, auth_token)
				message = client.messages \
								.create(
									body = contenu,
									from_ = settings.TWILIO_NUMBER,
									to = consultant_selectionne.profile.telephone
								)"""

			if (request.POST.get("message_email") == "true"):
				print('email')

			try:
				avatar = request.user.Profile_user.avatar.url
			except:
				avatar = None
			response_data['avatar'] = avatar
			response_data['message'] = contenu
			response_data['date'] = timezone.localtime().strftime('%e %B %Y %H:%M')

			bdd_messages.objects.create(
				user = request.user,
				consultant = consultant_selectionne,
				message = contenu,
			)
			p = Profile_user.objects.get(user = consultant_selectionne)
			p.dernier_message = timezone.localtime()
			p.save()

			response_data['rdm_couleur'] = request.user.profile.couleur_rdm
			response_data['diminutif'] = request.user.profile.diminutif

			return JsonResponse(response_data)

	for m in msg:
		if m.user.id == consultant_selectionne.id:
			m.lu = True
			m.save()

	context = locals()
	html_form = render_to_string('loadAjax/messagerie_administrateur_modal.html',context,request=request)
	return JsonResponse({'html_form': html_form})

def edit_adresse_modal(request):

	adresse_id = request.GET.get('id_adresse')
	adresse = Adresse_client.objects.get(id=adresse_id)

	context = locals()
	template = 'loadAjax/edit_adresse_modal.html'
	return render(request,template,context)

def edit_piece_jointe_modal(request):

	piece_jointe_id = request.GET.get('id_piece_jointe')
	piece_jointe = Piece_jointe_client.objects.get(id=piece_jointe_id)
	form_piece_jointe = ProfileClientPieceJointeForm(instance=piece_jointe)

	context = locals()
	template = 'loadAjax/edit_piece_jointe_modal.html'
	return render(request,template,context)

def edit_mission_type_modal(request):

	mission_type_id = request.GET.get('id_mission_type')
	mission_type = Mission_type_client.objects.get(id=mission_type_id)
	themes = Theme.objects.all()
	actu_theme = mission_type.theme.all()

	context = locals()
	template = 'loadAjax/edit_mission_type_modal.html'
	return render(request,template,context)

def ajax_utilisateurs(request):
	
	queryset = User.objects.all().order_by("-is_active").exclude(username = request.user.username)
	list = []

	for objects in queryset:
		try:
			avatar = objects.profile.avatar.url
		except:
			avatar = None;
		list.append({'pk':objects.id,'fields':
			{'username'  :objects.username,
			'first_name' :objects.first_name,
			'last_name'  :objects.last_name,
			'avatar'  	 :avatar,
			'diminutif'  :objects.profile.diminutif,
			'email'      :objects.email,
			'telephone'  :objects.profile.telephone,
			'date_joined':str(objects.date_joined),
			'last_login' :str(objects.last_login),
			'is_active'  :objects.is_active,
			'couleur_rdm':objects.profile.couleur_rdm,
			'groups'     :objects.groups.all()[0].name}})

	list_json = json.dumps(list)
	return HttpResponse(list_json, 'application/javascript')

def ajax_clients(request):
	
	queryset = Client.objects.all().order_by("-archive")
	list = []
	for objects in queryset:
		list.append({'pk':objects.id,'fields':
			{'nom'  :objects.nom,
			'couleur' :objects.code_couleur,
			'date_joined'  :str(objects.date_joined),
			'avatar'  	 :objects.avatar.url,
			'archive'      :objects.archive}})

	list_json = json.dumps(list)
	return HttpResponse(list_json, 'application/javascript')

def ajax_missions(request):
	
	queryset = Mission.objects.all()
	list = []
	for objects in queryset:
		if objects.consultant:
			consultant_id=objects.consultant.user.id
			consultant_avatar=objects.consultant.avatar.url
			consultant_prenom=objects.consultant.user.first_name
			consultant_nom=objects.consultant.user.last_name
			consultant_groups=objects.consultant.user.groups.all()[0].name
		else:
			consultant_id=None
			consultant_avatar=None
			consultant_prenom=None
			consultant_nom=None
			consultant_groups=None

		if objects.client:
			client_id=objects.client.id
			client_avatar=objects.client.avatar.url
			client_nom=objects.client.nom
		else:
			client_id=None
			client_avatar=None
			client_nom=None

		list.append({'pk':objects.id,'fields':
			{'jour'            :str(objects.jour_de_mission),
			'debut'            :str(objects.horaire_debut),
			'fin'              :str(objects.horaire_fin),
			'consultant_id'    :consultant_id,
			'consultant_avatar':consultant_avatar,
			'consultant_prenom':consultant_prenom,
			'consultant_nom'   :consultant_nom,
			'consultant_groups':consultant_groups,
			'client_id'        :client_id,
			'client_avatar'    :client_avatar,
			'client_nom'  	   :client_nom,
			'statut'  	       :objects.statut.nom,
			'type'             :objects.mission_type.nom}})

	list_json = json.dumps(list)
	return HttpResponse(list_json, 'application/javascript')

def ajax_contrats(request):
	
	queryset = Contrat.objects.all()
	
	list = []
	for objects in queryset:
		liste_avatar = []
		liste_mission = objects.mission_set.all()
		for obj in liste_mission:
			if obj.utilisateur:
				try:
					liste_avatar.append((True,obj.utilisateur.profile.avatar.url))
				except:
					liste_avatar.append((obj.utilisateur.profile.diminutif,obj.utilisateur.profile.couleur_rdm))

		list.append({'pk':objects.id,'fields':
			{'nom'  				:objects.nom,
			'date_debut' 			:str(objects.date_debut),
			'date_fin'  			:str(objects.date_fin),
			'client'  	 			:objects.client.nom,
			'avatar'				:liste_avatar,
			'id_client'  	 		:objects.client.id,
			'logo_client'  			:objects.client.avatar.url,
			'statut'      			:objects.statut.nom,
			'code_couleur_statut'	:objects.statut.code_couleur}})

	list_json = json.dumps(list)
	return HttpResponse(list_json, 'application/javascript')

def ajax_mission_consultant(request):
	
	queryset = Mission.objects.filter(consultant = request.user.profile)
	list = []
	for objects in queryset:

		if objects.is_client_visible and objects.client:
			client_id = objects.client.id
			client_avatar = objects.client.avatar.url
			client_nom = objects.client.nom
		else:
			client_id = None
			client_avatar = None
			client_nom = None

		if objects.is_misson_type_visible:
			mission_type = objects.mission_type.nom
		else:
			mission_type = None

		if objects.is_adresse_visible and objects.adresse_de_mission:
			adresse_nom = objects.adresse_de_mission.nom
			adresse_adresse = objects.adresse_de_mission.adresse
			adresse_ville = objects.adresse_de_mission.ville
			adresse_code = objects.adresse_de_mission.code_postal
		else:
			adresse_nom = None
			adresse_adresse = None
			adresse_ville = None
			adresse_code = None

		pjs = objects.piece_jointe_visible.all()
		pj_nom = []
		pj_document = []
		for pj in pjs:
			pj_nom.append(pj.nom)
			pj_document.append(pj.document.url)

		list.append({'pk':objects.id,'fields':
			{'jour'            :str(objects.jour_de_mission),
			'debut'            :str(objects.horaire_debut),
			'fin'              :str(objects.horaire_fin),
			'adresse_nom'      :adresse_nom,
			'adresse_adresse'  :adresse_adresse,
			'adresse_ville'    :adresse_ville,
			'adresse_code'     :adresse_code,
			'pj_nom'           :pj_nom,
			'pj_document'      :pj_document,
			'client_id'        :client_id,
			'client_avatar'    :client_avatar,
			'client_nom'  	   :client_nom,
			'statut'  	       :objects.statut.nom,
			'type'             :mission_type}})

	list_json = json.dumps(list)
	return HttpResponse(list_json, 'application/javascript')