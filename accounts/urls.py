from django.contrib import admin
from django.urls import path
from . import views

# le paramètre name est utilisé comme référence dans le href des url des pages selon {% url 'home' %}...
# path('Nom de chemain à taper dans la barre d'url de browser',Nom de chemain à traverser en backend par les href des links)

app_name = 'accounts'

urlpatterns = [
        path('signup',views.signup,name='signup'),
        path('profile',views.profile,name='profile'),
        path('profile/',views.adminProfile,name='admin_profile'),
        path('profile/edit',views.profile_edit,name='profile_edit'),
]
