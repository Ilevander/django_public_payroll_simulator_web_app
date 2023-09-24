from django import forms
from .models import Professeur,SitPaieProfEnsSec2Gr,RubDroitProfEnsSec2Gr,ListeGrade
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class ProfesseurForm(forms.ModelForm):

    """name = forms.CharField(widget=forms.TextInput(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    categorie = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    corps = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    cadre = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    grade = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    indice_echelon = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    region = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    localite = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    mutuelle = forms.CharField(widget=forms.Select(attrs={
         "class" : "input",
          "type" : "text",
          "placeholder" : "Aucun", 
    }),label="Nom")

    est_marie = forms.CharField(widget=forms.RadioSelect(attrs={
         "class" : "input",
          "type" : "radio",
          "placeholder" : "Séléctionner", 
    }),label="Nom")

    nombre_enfants = forms.CharField(widget=forms.NumberInput(attrs={
         "class" : "input",
          "type" : "number",
          "placeholder" : "Aucun", 
    }),label="Nom")"""

    class Meta:
        model = Professeur
        fields = [ 
            'name',
            'categorie',
            'corps',
            'cadre',
            'grade',
            'indice_echelon',
            'region',
            'localite',
            'mutuelle',
            'est_marie',
            'nombre_enfants',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'categorie': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'corps': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'cadre': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'grade': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'indice_echelon': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'region': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'localite': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Sélectionner'}),
            'mutuelle': forms.Select(attrs={'class': 'form-control mt-2', 'placeholder': 'Aucune'}),
            'est_marie': forms.RadioSelect(attrs={'class': 'radio mt-2 px-1', 'label': 'Situation Familiale'}),
            'nombre_enfants': forms.NumberInput(attrs={'class': 'form-control mt-2', 'style': 'width: 100px;', 'min': '1', 'max': '6'}),
        }
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Perform the calculations using the model's methods
        instance.traitement_base_calcul = instance.calculer_traitement_base()
        instance.indemnite_residence_calcul = instance.calculer_indemnite_residence()
        instance.total_calcul_indemnites = instance.calculer_total_indemnites()
        # Perform other calculations as needed...

        if commit:  
            instance.save()
        return instance    
  




class MonFormulaireDjango(forms.Form):
    CATEGORIES_CHOICES = [
        (1, "Personnel du Ministre de l'Enseignement Supérieur"),
        (2, "Autre"),
        (3, "Autre"),
    ]

    CORPS_CHOICES = [
        (2, "Enseignants chercheurs de l'enseignement supérieur"),
        (3, "Enseignants chercheurs de Médecine, de pharmacie et de médecine dentaire-NS"),
    ]

    CADRE_CHOICES = [
        (1, "Professeur de l'enseignement supérieur"),
        (2, "Professeur habilité"),
        (3, "Professeur agrégé"),
        (4, "Professeur Assistant"),
    ]

    GRADE_CHOICES = [
        (1, "Grade A"),
        (2, "Grade B"),
        (3, "Grade C"),
        (4, "Grade D"),
    ]

    INDICE_CHOICES = [
        (1, "760-01"),
        (2, "785-02"),
        (3, "810-03"),
        (4, "835-04"),
        # Add more choices as needed
    ]

    REGION_CHOICES = [
        (1, "Région Tanger-Tétouan-Al hoceima"),
        (2, "Région l'Oriental"),
        (3, "Région Fès-Meknès"),
        (4, "Région Rabat-Salé-Kénitra"),
        # Add more choices as needed
    ]

    LOCALITE_CHOICES = [
        (1, "Province d'Alhoceima (zone A)"),
        (2, "Province de Chaouèn (zone B)"),
        (3, "Province d'Ouezzane (zone B)"),
        (4, "Province Tanger-Assillah (zone C)"),
        # Add more choices as needed
    ]

    MUTUELLE_CHOICES = [
        (1, "MGPAP"),
        (2, "MGEN"),
        (3, "DOUANES"),
        (4, "POLICE"),
        # Add more choices as needed
    ]

    # Define form fields with choices
    categorie = forms.ChoiceField(choices=CATEGORIES_CHOICES,label='Categorie',initial='Séléctionner')
    corps = forms.ChoiceField(choices=CORPS_CHOICES,initial="Séléctionner")
    cadre = forms.ChoiceField(choices=CADRE_CHOICES)
    grade = forms.ChoiceField(choices=GRADE_CHOICES)
    indice = forms.ChoiceField(choices=INDICE_CHOICES)
    region = forms.ChoiceField(choices=REGION_CHOICES)
    localite = forms.ChoiceField(choices=LOCALITE_CHOICES)
    mutuelle = forms.ChoiceField(choices=MUTUELLE_CHOICES)
    marie = forms.BooleanField(required=False)
    nombre_enfants = forms.IntegerField(min_value=1, max_value=6)
    

class RegisterForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

'''class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=20,label='username')
    password = forms.CharField(max_length=20,label='password',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username","password"]'''


'''class RechercheRubriqueForm(forms.Form):
    libele_categorie = forms.ModelChoiceField(queryset=ListeFamilleGrade.objects.all(), empty_label="Select libele categorie")
    code_corp = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select code corp")
    code_cadre = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select code cadre")
    id_grade = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select id grade")
    code_grade = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select code grade")
    libele_grade = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select libele grade")
    code_comp = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select code comp")
    code_famgr = forms.ModelChoiceField(queryset=ListeFamilleGrade.objects.all(), empty_label="Select code famgr")
    echelle = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select echelle")
    poinindi = forms.ModelChoiceField(queryset=ListeGrade.objects.all(), empty_label="Select poinindi")

    def populate_dropdowns(self):
        # Populate dropdown choices for libele_categorie
        categories = ListeFamilleGrade.objects.all()
        self.fields['libele_categorie'].choices = [(cat.pk, cat.name) for cat in categories]

        # Populate dropdown choices for code_corp
        corps = ListeGrade.objects.all()
        self.fields['code_corp'].choices = [(corp.pk, corp.name) for corp in corps]

        cadre = ListeGrade.objects.all()
        self.fields['code_cadre'].choices = [(cdr.pk, cdr.name) for cdr in cadre]

        gradeId = ListeGrade.objects.all()
        self.fields['id_grade'].choices = [(grdId.pk, gradeId.name) for grdId in gradeId]

        gradeCode = ListeGrade.objects.all()
        self.fields['code_grade'].choices = [(grdCd.pk, grdCd.name) for grdCd in gradeCode]

        gradeLib = ListeGrade.objects.all()
        self.fields['libele_grade'].choices = [(grdLb.pk, grdLb.name) for grdLb in gradeLib]

        compCode = ListeGrade.objects.all()
        self.fields['code_comp'].choices = [(cmpCd.pk, cmpCd.name) for cmpCd in compCode]

        famgrCode = ListeFamilleGrade.objects.all()
        self.fields['code_famgr'].choices = [(fmgrCd.pk, fmgrCd.name) for fmgrCd in famgrCode]

        echll = ListeGrade.objects.all()
        self.fields['echelle'].choices = [(ech.pk, ech.name) for ech in echll]

        pnd = ListeGrade.objects.all()
        self.fields['poinindi'].choices = [(pn.pk, pn.name) for pn in pnd]'''


class SitPaieProfForm(forms.Form):
    
    libecate = forms.ModelChoiceField(queryset=ListeGrade.objects.values_list('libecate', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='Catégorie')
    libegrad = forms.ModelChoiceField(queryset=ListeGrade.objects.values_list('libegrad', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='Grade')
    idengrad = forms.ModelChoiceField(queryset=SitPaieProfEnsSec2Gr.objects.values_list('idengrad', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='ID Grade')
    idendroi = forms.ModelChoiceField(queryset=SitPaieProfEnsSec2Gr.objects.values_list('idendroi', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='ID Droit')
    idencomb = forms.ModelChoiceField(queryset=SitPaieProfEnsSec2Gr.objects.values_list('idencomb', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='ID Comb')
    echelon = forms.ModelChoiceField(queryset=SitPaieProfEnsSec2Gr.objects.values_list('echelon', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    codezone = forms.ModelChoiceField(queryset=SitPaieProfEnsSec2Gr.objects.values_list('codezone', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='Code de Zone')
    coderubr = forms.ModelChoiceField(queryset=RubDroitProfEnsSec2Gr.objects.values_list('coderubr', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='Rubrique')
    codecomp = forms.ModelChoiceField(queryset=ListeGrade.objects.values_list('codecomp', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    codfamgr = forms.ModelChoiceField(queryset=ListeGrade.objects.values_list('codfamgr', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False,label='Code Famille Grade')
    poinindi = forms.ModelChoiceField(queryset=ListeGrade.objects.values_list('poinindi', flat=True).distinct(), widget=forms.Select(attrs={'class': 'form-control'}),required=False)

