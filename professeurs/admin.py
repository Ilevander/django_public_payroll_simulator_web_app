from django.contrib import admin
from .models import Professeur,Rubrique,ListeGrade,ListeFamilleGrade,ListeGradeFamilleGrade,RubDroitProfEnsSec2Gr,SitPaieProfEnsSec2Gr

# Register your models here.

admin.site.register(Professeur)
admin.site.register(Rubrique)
admin.site.register(ListeGrade)
admin.site.register(ListeFamilleGrade)
admin.site.register(ListeGradeFamilleGrade)
admin.site.register(RubDroitProfEnsSec2Gr)
admin.site.register(SitPaieProfEnsSec2Gr)
admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'Data Base'