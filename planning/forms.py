from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.core.files.images import get_image_dimensions

from django.core.mail import send_mail

from .models import *

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile_user
		fields = ('avatar',)
		widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            }

class ProfileClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ('avatar',)
		widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            }

class ProfileClientPieceJointeForm(forms.ModelForm):
	class Meta:
		model = Piece_jointe_client
		fields = ('document',)
		widgets = {
            'document': forms.FileInput(),
            }

class ProfileClientAddPieceJointeForm(forms.ModelForm):
	class Meta:
		model = Piece_jointe_client
		fields = ('document',)
		widgets = {
            'document': forms.FileInput(attrs={'class':'custom-file-input','id': 'id_add_document','required':""}),
            }