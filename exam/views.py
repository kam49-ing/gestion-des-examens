from django.shortcuts import render, redirect
from exam.forms import RegisterForm, LoginForm, ChangePasswordForm, AjoutNoteForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, password_changed, password_validators_help_texts
from django import forms
from exam.models import Niveau, Filiere, Matiere

def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        if len(User.objects.filter(id=request.session['logged_user_id'])) == 1:
            return User.objects.get(id=request.session['logged_user_id'])
    return None
def index(request):
    if get_logged_user_from_request:
        return render(request, 'index.html')
    else:
        return redirect('/login')
def connexion(request):
    if len(request.POST) > 1:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username and password:
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    logged_user = User.objects.get(username = username)
                    request.session['logged_user_id'] = logged_user.id
                    return redirect('/index')
                else:
                    form.non_field_errors = 'Nom d\'utilisateur ou mot de passe incorrect'
                    return render(request, 'login.html', { 'form': form })
        else:
            return render(request, 'login.html', { 'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def register(request):
    if len(request.POST)>1:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            if(password == password1):
                try:
                    validate_password(password)
                except forms.ValidationError as errors:
                    for error in errors:
                        if  'password' in form.errors:
                            form.errors['password'] = form.errors['password'] +' '+ error
                        else:
                            form.errors['password'] = error
                    return render(request, 'register.html', {'form': form})
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return redirect('/index')
            else:
                form.errors['password1'] = "Les mots de passe ne correspondent pas. "
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('/login')

def changePassword(request):
    if get_logged_user_from_request(request):
        logged_user=get_logged_user_from_request(request)
        if len(request.POST) > 1:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                old_password = form.cleaned_data['old_password']
                new_password = form.cleaned_data['new_password']
                new_password_confirmation = form.cleaned_data['new_password_confirmation']
                if new_password != new_password_confirmation:
                    form.errors['new_password_confirmation'] = 'Les mots de passe ne correspondent pas'
                    return render(request, 'changepassword.html', {'form':form})
                if logged_user.check_password(old_password):
                    form.errors['old_password'] = 'Mot de passe erroné'
                    return render(request, 'changepassword.html', {'form':form})
                logged_user.set_password(new_password)
                try:
                   password_changed(password, logged_user)
                except forms.ValidationError as errors:
                    for error in errors:
                        if 'password' in request.errors:
                            request.errors['password'] = request.errors['password'] + ' '+ error
                        else:
                            request.errors['new_password'] = error
                    return render(request, 'changepassword.html', {'form': form})
        else:
            form = ChangePasswordForm()
            return render(request, 'changepassword.html', {'form': form})
    else:
        return redirect('/login')

def note(request):
    if get_logged_user_from_request(request):
        if len(request.POST)>1:
            form = AjoutNoteForm(request.POST)
        else: 
            form = AjoutNoteForm()
            niveaux = Niveau.objects.all()
            return render(request, 'ajoutnote.html', {'form': form, 'niveaux': niveaux})
    else:
        return redirect('/login')
def exemple(request):
    return redirect('/index')