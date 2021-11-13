# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Filiere(models.Model):
    libelle = models.CharField(max_length = 30)
    def __str__(self):
        return self.libelle

class Niveau(models.Model):
    libelle = models.CharField(max_length = 30)
    def __str__(self):
        return self.libelle

class Module(models.Model):
    libelle = models.CharField(max_length = 30)
    filiere = models.ManyToManyField(Filiere)
    def __str__(self):
        return self.libelle

class Annee(models.Model):
    libelle = models.CharField(max_length = 30)
    def __str__(self):
        return self.libelle

class Matiere(models.Model):
    libelle = models.CharField(max_length = 30)
    coefficient = models.IntegerField()
    annee = models.ManyToManyField(Annee)
    module = models.ManyToManyField(Module)
    def __str__(self):
        return self.libelle
   
class Controle(models.Model):
    libelle = models.CharField(max_length = 30)
    id_matiere = models.ForeignKey(Matiere, on_delete= models.CASCADE)
    annee = models.ManyToManyField(Annee)
    def __str__(self):
        return self.libelle

class Examen(models.Model):
    libelle = models.CharField(max_length = 30)
    id_matiere = models.ForeignKey(Matiere, on_delete= models.CASCADE)
    annee = models.ManyToManyField(Annee)
    def __str__(self):
        return self.libelle



class Notation(models.Model):
    libelle = models.IntegerField()
    def __str__(self):
        return self.libelle

class Question(models.Model):
    libelle = models.TextField()
    id_controle = models.ForeignKey(Controle, on_delete= models.CASCADE)
    notation = models.IntegerField()
    def __str__(self):
        return self.libelle

class Reponse(models.Model):
    libelle = models.TextField()
    id_question = models.ForeignKey(Question, on_delete= models.CASCADE)
    def __str__(self):
        return self.libelle

class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    id_niveau = models.ForeignKey(Niveau, on_delete= models.CASCADE)
    id_filiere = models.ForeignKey(Filiere, on_delete= models.CASCADE)
    reponse = models.ManyToManyField(Reponse, null = True, blank=True)
    controle = models.ManyToManyField(Controle, null = True, blank=True)
    examen = models.ManyToManyField(Examen, null = True, blank = True)
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name

class Moyenne(models.Model):
    libelle = models.FloatField()
    id_candidat = models.ForeignKey(Candidat, on_delete = models.CASCADE)
    def __str__(self):
        return self.libelle

class MoyenneModule(models.Model):
    libelle = models.FloatField()
    id_candidat = models.ForeignKey(Candidat, on_delete = models.CASCADE)
    id_module = models.ForeignKey(Module, on_delete= models.CASCADE)
    def __str__(self):
        return self.libelle

class MoyenneMatiere(models.Model):
    libelle = models.FloatField()
    id_candidat = models.ForeignKey(Candidat, on_delete = models.CASCADE)
    id_matiere = models.ForeignKey(Matiere, on_delete= models.CASCADE)
    def __str__(self):
        return self.libelle

class Note(models.Model):
    libelle = models.FloatField()
    id_candidat = models.ForeignKey(Candidat, on_delete = models.CASCADE)
    id_moyenne = models.ForeignKey(Moyenne, on_delete= models.CASCADE)
    id_controle = models.ForeignKey(Controle, on_delete= models.CASCADE)
    def __str__(self):
        return self.libelle

class NoteExamen(models.Model):
    libelle = models.FloatField()
    id_candidat = models.ForeignKey(Candidat, on_delete = models.CASCADE)
    id_moyenne  = models.ForeignKey(Moyenne, on_delete = models.CASCADE)
    id_examen = models.ForeignKey(Examen, on_delete = models.CASCADE)
    def __str__(self):
        return self.libelle

class ReponseExacte(models.Model):
    id_reponse = models.ForeignKey(Reponse, on_delete= models.CASCADE)

