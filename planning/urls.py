from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^permission/', views.erreur_403, name='permission'),
    url(r'^reglages/', views.reglages, name='reglages'),


    url(r'^planning/', views.planning, name='planning'),

    ##### administrateur
    url(r'^utilisateurs/', views.utilisateurs, name='utilisateurs'),


    url(r'^profil_utilisateur/(?P<datapk>\w+)/', views.profil_utilisateur, name='profil_utilisateur'),

    url(r'^client/', views.client, name='client'),
    url(r'^profil_client/(?P<datapk>\w+)/', views.profil_client, name='profil_client'),




    url(r'^mission', views.mission, name='mission'),
    url(r'^profil_mission/(?P<datapk>\w+)/', views.profil_mission, name='profil_mission'),

    ##### consultant
    url(r'^consultant/mission_consultant', views.mission_consultant, name='mission_consultant'),

    ##### ajax
    url(r'^ajax_utilisateurs', views.ajax_utilisateurs, name='ajax_utilisateurs'),
    url(r'^ajax_clients', views.ajax_clients, name='ajax_clients'),
    url(r'^ajax_missions$', views.ajax_missions, name='ajax_missions'),
    url(r'^ajax_mission_consultant$', views.ajax_mission_consultant, name='ajax_mission_consultant'),


    url(r'^loadAjax/messagerie_administrateur_modal', views.messagerie_administrateur_modal, name='messagerie_administrateur_modal'),
    url(r'^loadAjax/edit_competence_modal', views.edit_competence_modal, name='edit_competence_modal'),
    url(r'^loadAjax/edit_adresse_modal', views.edit_adresse_modal, name='edit_adresse_modal'),
    url(r'^loadAjax/edit_piece_jointe_modal', views.edit_piece_jointe_modal, name='edit_piece_jointe_modal'),
    url(r'^loadAjax/edit_mission_type_modal', views.edit_mission_type_modal, name='edit_mission_type_modal'),

    #### messagerie
    url(r'^messagerie/$', views.messagerie_administrateur, name='messagerie_administrateur'),
    url(r'^messagerie-consultant/', views.messagerie_consultant, name='ma_messagerie'),
    #url(r'^sms/$', views.sms, name='sms'),
]