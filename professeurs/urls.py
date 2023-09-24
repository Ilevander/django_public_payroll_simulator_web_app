from django.contrib import admin
from django.urls import path
from .views import About,Home,Blogs,Texte,Index,Form,Afficher_resultats_calculs,combined_data_view,selected_data_view,liberubr_list_view,generate_pdf #userLogin

# le paramètre name est utilisé comme référence dans le href des url des pages selon {% url 'home' %}...
# path('Nom de chemain à taper dans la barre d'url de browser',Nom de chemain à traverser en backend par les href des links)

urlpatterns = [
    path('', Home,name='home'),
    path('about/', About,name='about'),
    #path('login/',userLogin,name='login'),
    path('blogs/',Blogs,name='blogs'),      
    path('texte/',Texte,name='texte'),
    path('index/',Index,name='dashboard'),
    path('form2/',Form,name='form2'),
    path('result/',Afficher_resultats_calculs,name='result'),
    path('combined-data/', combined_data_view, name='combined-data'),
    path('selected-data/',selected_data_view, name='selected-data'),
    path('liberubr-list/',liberubr_list_view, name='liberubr-list'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
]
