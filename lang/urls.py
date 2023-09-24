from django.urls import path
from . import views

app_name = 'lang'

urlpatterns = [
    path('acceuil',views.acceuil,name='acceuil'),
]
