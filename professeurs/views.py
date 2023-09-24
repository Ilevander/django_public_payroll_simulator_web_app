from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Professeur,SitPaieProfEnsSec2Gr,RubDroitProfEnsSec2Gr,ListeFamilleGrade,ListeGrade
from .forms import ProfesseurForm,MonFormulaireDjango,SitPaieProfForm  
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import psycopg2
from django.db.models import Sum
from django.urls import reverse
import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def About(request):
    return render(request,'about.html')

def Home(request):
    return render(request,'home.html')



def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')



def Blogs(request):
    return render(request,'blogs.html')

def Texte(request):
    return render(request,'texte.html')

def Form (request):
    if request.method == 'POST': #Pour des raison de sécurité
        form = ProfesseurForm(request.POST)
        if form.is_valid():#ne pas enregistrer ssi les informations sont valide (eviter les attack js)
            form.save()
            # Optionally, you can add a success message or redirect to another page
            # return redirect('success_page')
    else:
        form = ProfesseurForm()

    return render(request, 'form.html', {'form': form})


"""def create_professeur(request):
    if request.method == 'POST':
        form = ProfesseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after saving the data.
    else:
        form = ProfesseurForm()
    
    return render(request, 'form.html', {'form': form})"""


def ma_vue(request):
    if request.method == 'POST':
        form = MonFormulaireDjango(request.POST)
        if form.is_valid():
            # Handle form submission here
            return render(request, 'success_page.html')
    else:
        form = MonFormulaireDjango()

    return render(request, 'form.html', {'form': form})


"""def Test(request):
    data = ProfesseurForm(request.POST)
    data.save()"""
"""categorie = request.POST.get('categorie')
    corps = request.POST.get('corps')
    cadre = request.POST.get('cadre')
    grade = request.POST.get('grade')
    #indice = request.POST.get('indice')
    region = request.POST.get('region')
    mutuelle = request.POST.get('mutuelle')
    #marie = request.POST.get('marie')
    nombre_enfants = request.POST.get('nombre_enfant')
    data = Professeur(categorie=categorie,corps=corps,cadre=cadre,grade=grade,region=region,mutuelle=mutuelle,nombre_enfants=nombre_enfants)"""
     
"""return render(request,'test.html' , {'key_test':ProfesseurForm})"""

"""def Test(request):
    if request.method == 'POST': #Pour des raison de sécurité
        form = ProfesseurForm(request.POST)
        if form.is_valid():#ne pas enregistrer ssi les informations sont valide (eviter les attack js)
            form.save()
            # Optionally, you can add a success message or redirect to another page
            # return redirect('success_page')
    else:
        form = ProfesseurForm()

    return render(request, 'test.html', {'form': form})"""

def Afficher_resultats_calculs(request):
    # Récupérer toutes les instances de Professeur ou les instances nécessaires selon vos besoins
    professeurs = Professeur.objects.all()
    
    # Effectuer les calculs pour chaque instance de professeur
    for professeur in professeurs:
        professeur.traitement_base_calcul = professeur.calculer_traitement_base()
        professeur.indemnite_residence_calcul = professeur.calculer_indemnite_residence()
        professeur.total_calcul_indemnites = professeur.calculer_total_indemnites()
        professeur.allocation_calcul_familial= professeur.calculer_allocation_familiale()
        professeur.indemnite_calcul_encadrement= professeur.calculer_indemnite_encadrement()
        professeur.indemnite_recherche_applicue_calculer= professeur.calculer_indemnite_recherche_appliquee()
        professeur.indemnite_calcule_risque= professeur.calculer_indemnite_risque()
        professeur.total_calcule_indemnites= professeur.calculer_total_indemnites()
        professeur.total_calculer_mensuel_brut= professeur.calculer_total_mensuel_brut()
        professeur.cotisation_calcule_mutuelle= professeur.calculer_cotisation_mutuelle()
        professeur.cotisation_calcul_amo= professeur.calculer_cotisation_amo()
        professeur.calcul_sm_cotisation= professeur.calculer_cotisation_sm()
        professeur.calcul_cdd_cotisation= professeur.calculer_cotisation_ccd()
        professeur.total_calculer_cotisation= professeur.calculer_total_cotisations()
        professeur.impot_calcule_revenu= professeur.calculer_impot_revenu()
        professeur.salaire_calcule_brut= professeur.calculer_salaire_brut()
        professeur.net_calculer_imposable= professeur.calculer_net_imposable()
        professeur.total_calcule_revenu= professeur.calculer_total_revenus()
        professeur.salaire_net_calcule= professeur.calculer_salaire_net()
        professeur.frais_calculer_professionnels= professeur.calculer_frais_professionnels()

    # Passer les instances de professeur avec les résultats des calculs à la template
    context = {
        'professeurs': professeurs,
    }

    return render(request,'result.html', context)

## -- Authentification : -- ##



'''def userLogin(request):
    if request.method == "POST":
      form = LoginForm()
      inUsername = request.POST.get('username')
      inpPassword = request.POST.get('password')
      user = authenticate(request,username=inUsername, password=inpPassword)
      if user is not None: #si la variable user n'est pas null , None en django indique null . Donc si la variable contienne des données
         login(request,user)
         return redirect('professeurs:form2')
    else:
        form = LoginForm() #Sinon retourner le forme de login lui même
    return render(request,'login.html',{'form':form}) # render le contexte {'form':form} dans login.html'''


'''def recherche_rubrique(request):
    form = RechercheRubriqueForm()  # Create an instance of the form
    if request.method == 'POST':
        form = RechercheRubriqueForm(request.POST)  # Bind form data to the POST data
        if form.is_valid():
            libele_categorie = request.POST['libele_categorie']
            code_corp = request.POST['code_corp']
            code_cadre = request.POST['code_cadre']
            id_grade = request.POST['id_grade']
            code_grade = request.POST['code_grade']
            libele_grade = request.POST['libele_grade']
            code_comp = request.POST['code_comp']
            code_famgr = request.POST['code_famgr']
            echelle = request.POST['echelle']
            poinindi = request.POST['poinindi']

        try:
            rubrique = SitPaieProfEnsSec2Gr.objects.get(
                libele_catégorie=libele_categorie,
                code_corp=code_corp,
                code_cadre=code_cadre,
                id_grade=id_grade,
                libele_grade=libele_grade,
                code_comp=code_comp,
                code_famgr=code_famgr,
                echelle=echelle,
                poinindi=poinindi,
            )

            rubriques = [
                {
                    'libele_rubrique': rubrique.libele_rubrique,
                    'montant_mensuel': rubrique.montant_octr / 12,
                }
            ]
        except SitPaieProfEnsSec2Gr.DoesNotExist:
            conn = psycopg2.connect(
                dbname="simulateur",
                user="root",
                password="ilyass@123",
                host="127.0.0.1",
                port="5432"
            )
            cursor = conn.cursor()

            query = """
                        SELECT
                            sp.liberubr,
                            sp.montoctr / 12 AS montant_mensuel
                        FROM
                            "sit_paie_prof_ens_sec_2_gr" sp
                        JOIN
                            "rub_droit_prof_ens_sec_2_gr" rd1
                            ON sp.coderubr = rd1.coderubr
                        JOIN
                            "liste_grade_famille_grade" gf
                            ON sp.codfamgr = gf.codfamgr
                        JOIN
                            "liste_famille_grade" fg
                            ON gf.codfamgr = fg.codfamgr
                        JOIN
                            "liste_grade" lg
                            ON sp.idengrad = lg.idengrad
                        WHERE
                            sp.idengrad = %s
                            AND sp.codfamgr = %s
                            AND sp.libegrad = %s
                            AND sp.coderubr = %s
                    """

            cursor.execute(query, (
                    libele_categorie, code_corp, code_cadre, id_grade, code_grade, libele_grade, code_comp, code_famgr, echelle, poinindi
                ))
            results = cursor.fetchall()

            conn.close()

            rubriques = []
            for row in results:
                    rubrique = {
                        'libele_rubrique': row[0],
                        'montant_mensuel': row[1]
                    }
                    rubriques.append(rubrique)

        return render(request, 'resultats.html', {'rubriques': rubriques})

    else:
        form = RechercheRubriqueForm()

    return render(request, 'form.html', {'form': form})
'''

'''def data_view(request):
   sit_paie_data = SitPaieProfEnsSec2Gr.objects.values('montoctr', 'liberubr')
   rub_droit_data = RubDroitProfEnsSec2Gr.objects.values('coderubr', 'liberubr')

    context = {
        'sit_paie_data': sit_paie_data,
        'rub_droit_data': rub_droit_data,
    }

    return render(request, 'data_template.html', context)'''

def combined_data_view(request):
    combined_data = SitPaieProfEnsSec2Gr.objects.values(
        'coderubr', 'liberubr', 'idengrad'
    ).annotate(total_montoctr=Sum('montoctr'))

    for entry in combined_data:
        coderubr = entry['coderubr']
        liberubr = entry['liberubr']
        idengrad = entry['idengrad']

        related_rows = SitPaieProfEnsSec2Gr.objects.filter(
            coderubr=coderubr, liberubr=liberubr, idengrad=idengrad
        )

        entry['related_rows'] = related_rows

    context = {
        'combined_data': combined_data
    }

    return render(request, 'combined_data_template.html', context)



@login_required #N'appliquer la methode ssi la le user est logé
def selected_data_view(request):
    if request.method == 'GET':
        form = SitPaieProfForm(request.GET)

        if form.is_valid():
            idendroi = form.cleaned_data['idendroi']
            idengrad = form.cleaned_data['idengrad']
            idencomb = form.cleaned_data['idencomb']
            codfamgr = form.cleaned_data['codfamgr']
            echelon = form.cleaned_data['echelon']
            codezone = form.cleaned_data['codezone']
            coderubr = form.cleaned_data['coderubr']            

            filters = {
                'idendroi': idendroi,
                'idengrad':idengrad,
                'idencomb': idencomb,
                'codfamgr': codfamgr,
                'echelon' : echelon,
                'codezone': codezone,
                'coderubr': coderubr,                 
            }

            if idengrad != '':
                filters['idengrad'] = idengrad

            if echelon != '':
                filters['echelon'] = echelon


            if idendroi != '':
                filters['idendroi'] = idendroi   

            if idencomb != '':
                filters['idencomb'] = idencomb 
            
            if codfamgr != '':
                filters['codfamgr'] = codfamgr

            if codezone != '':
                filters['codezone'] = codezone

            if coderubr != '':
                filters['coderubr'] = coderubr       

            combined_data = SitPaieProfEnsSec2Gr.objects.filter(**filters)
        else:
            combined_data = SitPaieProfEnsSec2Gr.objects.all()

    else:
        form = SitPaieProfForm()
        combined_data = SitPaieProfEnsSec2Gr.objects.all()

    # Fetch distinct values for libfamgr and echelle fields from ListeFamilleGrade
    libfamgr_choices = ListeFamilleGrade.objects.values_list('libfamgr', flat=True).distinct()
    echelle_choices = ListeFamilleGrade.objects.values_list('echelle', flat=True).distinct()
    coderubr_choices = RubDroitProfEnsSec2Gr.objects.values_list('coderubr', flat=True).distinct()
    naturubr_choices = RubDroitProfEnsSec2Gr.objects.values_list('naturubr', flat=True).distinct()

    context = {
        'combined_data': combined_data,
        'form': form,
        'libfamgr_choices': libfamgr_choices,
        'echelle_choices': echelle_choices,
        'coderubr_choices':coderubr_choices,
        'naturubr_choices':naturubr_choices,
    }

    return render(request, 'selected_data_template.html', context)




def liberubr_list_view(request):
    liberubr_coderubr_list = RubDroitProfEnsSec2Gr.objects.values_list('liberubr', 'coderubr')
    liberubr_montoctr_list = SitPaieProfEnsSec2Gr.objects.values_list('liberubr', 'montoctr')

    context = {
        'liberubr_coderubr_list': liberubr_coderubr_list,
        'liberubr_montoctr_list': liberubr_montoctr_list,
    }

    return render(request, 'liberubr_list_template.html', context) 




def generate_pdf(request):
    template_path = 'pdf_view.html'  # Replace with the actual path to your template

     # Query only the specific fields needed for liberubr_coderubr_list
    liberubr_coderubr_list = RubDroitProfEnsSec2Gr.objects.values_list('liberubr', 'coderubr')
    
    # Query only the specific fields needed for liberubr_montoctr_list
    liberubr_montoctr_list = SitPaieProfEnsSec2Gr.objects.values_list('liberubr', 'montoctr')

    context = {
        'liberubr_coderubr_list': liberubr_coderubr_list,
        'liberubr_montoctr_list': liberubr_montoctr_list,
    }

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="liberubr_list.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation error')

    return response