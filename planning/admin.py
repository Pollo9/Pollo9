from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User , Permission
from .models import *




#LE CLIENT
class Mission_type_clientInline(admin.TabularInline):
    model = Mission_type_client
    extra = 0

class Adresse_clientInline(admin.TabularInline):
    model = Adresse_client
    extra = 0

class Piece_jointe_clientInline(admin.TabularInline):
    model = Piece_jointe_client
    extra = 0
  

class ClientAdmin(admin.ModelAdmin):

    model = Client
    fieldsets = [
        ('INFORMATIONS',               {'fields': ['nom','telephone','email','site_web','code_couleur','date_joined','avatar','archive']}),
    ]

    inlines = [Mission_type_clientInline,Adresse_clientInline,Piece_jointe_clientInline]

    
    list_display = ('nom', 'code_couleur', 'date_joined', 'avatar', 'archive')
    list_filter = ['nom']
    search_fields = ['nom']


admin.site.register(Client, ClientAdmin)


#LES PETITES BDD
class ThemeAdmin(admin.ModelAdmin):
    list_filter = ['nom']
    search_fields = ['nom']

admin.site.register(Theme, ThemeAdmin)

class Statut_missionAdmin(admin.ModelAdmin):
    list_filter = ['nom']
    search_fields = ['nom']

admin.site.register(Statut_mission, Statut_missionAdmin)

class bdd_messagesAdmin(admin.ModelAdmin):
    list_filter = ['message']
    search_fields = ['message']

admin.site.register(bdd_messages, bdd_messagesAdmin)

admin.site.register(Mission_type_client)

admin.site.register(Jour_semaine)
admin.site.register(Jour_bloque)
admin.site.register(Statut_contrat)
admin.site.register(Statut_journee)
#LE PROFILE CONSULTANT
class CompetenceInline(admin.TabularInline):
    model = Competence
    extra = 0


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Profile_userInline(admin.StackedInline):
    fieldsets = [
        ('INFORMATIONS',               {'fields': ['user','diminutif','avatar','archive']}),
        ('CONTACT ET ADRESSE',               {'fields': ['telephone','ville','code_postal','adresse']})
    ]
    model = Profile_user
    can_delete = False
    verbose_name_plural = 'consultants'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Profile_userInline,CompetenceInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Permission)

#LES MISSIONS
class Document_renduInline(admin.TabularInline):
    model = Document_rendu
    extra = 0

class Document_supplementaireInline(admin.TabularInline):
    model = Document_supplementaire
    extra = 0

class MissionAdmin(admin.ModelAdmin):

    model = Mission
    fieldsets = [
        ('INFORMATIONS',               {'fields': ['contrat','mission_type','adresse','document','statut']}),
    ]

    inlines = [Document_renduInline,Document_supplementaireInline]

    
    list_display = ('contrat', 'utilisateur', 'mission_type')
    list_filter = ['mission_type']
    search_fields = ['mission_type']

admin.site.register(Mission, MissionAdmin)

#LES CONTRATS
class MissionInline(admin.TabularInline):
    model = Mission
    extra = 0

class ContratAdmin(admin.ModelAdmin):

    model = Contrat
    fieldsets = [
        ('INFORMATIONS',               {'fields': ['nom','client','date_debut','date_fin','statut']}),
    ]

    inlines = [MissionInline]

    
    list_display = ('nom', 'date_debut', 'date_fin')
    list_filter = ['nom']
    search_fields = ['nom']


admin.site.register(Contrat, ContratAdmin)