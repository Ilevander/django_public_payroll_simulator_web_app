from django.urls import path
from . import views

# le paramètre name est utilisé comme référence dans le href des url des pages selon {% url 'home' %}...
# path('Nom de chemain à taper dans la barre d'url de browser',Nom de chemain à traverser en backend par les href des links)

app_name = 'contact'

urlpatterns = [
        path('contact-us/',views.send_message,name='contact-us'),
]



