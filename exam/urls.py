# -*- encoding: utf-8 -*-
"""
exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from exam.views import index, connexion, register, deconnexion, changePassword, note, exemple
#change password
from django.contrib.auth.views import PasswordChangeView
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', index),
    url('^login$', connexion),
    url('^register', register),
    url('^index$', index),
    path('logout/', deconnexion),
    url('password-change', PasswordChangeView),
    url('^note$', note),
    url('^ajax_exemple$', exemple)
    #change password with django.contrib.auth
    #path('password_change/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]

## django-cruds-adminlte
#from cruds_adminlte.urls import crud_for_app
#urlpatterns += crud_for_app('exam')