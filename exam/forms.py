# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom d\'utilisateur'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'}))
class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 30, label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom d\'utilisateur'}))
    email = forms.EmailField(label='Courriel', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Courriel'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholdeer':'Mot de passe'}))
    password1 = forms.CharField(label='Retapez le mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Retapez le mot de passe'}))
    first_name = forms.CharField(label='Prénoms', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prenoms'}))
    last_name = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}))
    
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Ancien mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ancien Mot de passe'}))
    new_password = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Nouveau mot de passe'}))
    new_password_confirmation = forms.CharField(label='Confirmation du nouveau mot de passe', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmation du nouveau mot de passe'}))

class AjoutNoteForm(forms.Form):
    libelle = forms.FloatField(label='Note', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'12.5'}))