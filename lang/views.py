from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def acceuil(request):
    trans = translate(language='fr')
    return render(request,'acceuil.html',{'trans':trans})



def translate(language):
    cur_languagge = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_languagge)
    return text    


def switch_language(request, language_code):
    # Set the selected language in the session
    request.session['django_language'] = language_code
    return HttpResponseRedirect(reverse('home'))
