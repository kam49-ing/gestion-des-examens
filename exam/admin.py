from django.contrib import admin
from django.apps import apps
from exam.models import *
from django.db.models import Model

#for value in apps.all_models['exam'].values():
#    if 'Relations' not in value:
#        admin.site.register(value)


#models = apps.get_models()

#for model in models:
#    admin.site.register(model)
admin.site.register(Candidat)
admin.site.register(Filiere)
admin.site.register(Matiere)
admin.site.register(Annee)
admin.site.register(Module)
admin.site.register(Examen)
admin.site.register(NoteExamen)
admin.site.register(Note)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(ReponseExacte)
admin.site.register(Controle)
admin.site.register(MoyenneMatiere)
admin.site.register(MoyenneModule)
admin.site.register(Niveau)
admin.site.register(Notation)