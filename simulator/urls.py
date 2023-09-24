"""
URL configuration for simulator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

#to change language
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),

]

urlpatterns += i18n_patterns (
    path('accounts/', include('django.contrib.auth.urls')),# Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('admin/', admin.site.urls),
    path('',include('professeurs.urls')),#include pour toutes les urls de l'application professeurs
    path('',include('lang.urls',namespace='lang')),
    path('',include('django.contrib.auth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
