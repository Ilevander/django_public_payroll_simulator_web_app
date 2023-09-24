from django.db import models
from datetime import datetime,date
from django.core.exceptions import ValidationError
from django.core.validators import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Professeur(models.Model):
    name = models.CharField(max_length=50,verbose_name='Nom')
    CATEGORIE_CHOICES = (
        ('Personnel de ministre de l\'enseignement supérieur', 'Personnel de ministre de l\'enseignement supérieur'),
        # Ajoutez d'autres choix de catégorie ici si nécessaire
    )

    CORPS_CHOICES = (
        ('Corps des enseignants chercheurs de l\'enseignement supérieur', 'Corps des enseignants chercheurs de l\'enseignement supérieur'),
        ('Enseignant chercheurs de l\'enseignement supérieur', 'Enseignant chercheurs de l\'enseignement supérieur'),
        ('Enseignants chercheurs de la médecine, la pharmacie et de médecine dentaire-NS', 'Enseignants chercheurs de la médecine, la pharmacie et de médecine dentaire-NS'),
        # Ajoutez d'autres choix de corps ici si nécessaire
    )

    CADRE_CHOICES = (
        ('Professeur de l\'enseignement supérieur', 'Professeur de l\'enseignement supérieur'),
        ('Professeur habilite', 'Professeur habilite'),
        ('Professeur assistant', 'Professeur assistant'),
        ('Professeur agrégé', 'Professeur agrégé'),
        # Ajoutez d'autres choix de cadre ici si nécessaire
    )

    GRADE_CHOICES = (
        ('Grade A', 'Grade A'),
        ('Grade B', 'Grade B'),
        ('Grade C', 'Grade C'),
        ('Grade D', 'Grade D'),
        # Ajoutez d'autres choix de grade ici si nécessaire
    )

    INDICE_ECHELON_CHOICES = (
    # Enseignant chercheurs de l'enseignement supérieur avec le cadre Professeur de l'enseignement supérieur
    ('760-01', '760-01'),
    ('785-02', '785-02'),
    ('810-03', '810-03'),
    ('835-04', '835-04'),
    # Enseignant chercheurs de l'enseignement supérieur avec le cadre Professeur habité
    ('580-01', '580-01'),
    ('620-02', '620-02'),
    ('660-03', '660-03'),
    ('720-04', '720-04'),
    # Enseignant chercheurs de l'enseignement supérieur avec le cadre Professeur assistant
    ('509-01', '509-01'),
    ('542-02', '542-02'),
    ('574-03', '574-03'),
    ('606-04', '606-04'),
    # Enseignants chercheurs de la médecine, la pharmacie et de médecine dentaire-NS avec le cadre Professeur agrégé
    ('760-05', '760-05'),  # Note that I've changed '580-01' to '760-05' to make it unique
    ('785-06', '785-06'),  # Note that I've changed '620-02' to '785-06' to make it unique
    ('810-07', '810-07'),  # Note that I've changed '660-03' to '810-07' to make it unique
    ('835-08', '835-08'),  # Note that I've changed '720-04' to '835-08' to make it unique
    # Enseignants chercheurs de la médecine, la pharmacie et de médecine dentaire-NS avec le cadre Professeur assistant
    ('509-09', '509-09'),  # Note that I've changed '509-01' to '509-09' to make it unique
    ('542-10', '542-10'),  # Note that I've changed '542-02' to '542-10' to make it unique
    ('574-11', '574-11'),  # Note that I've changed '574-03' to '574-11' to make it unique
    ('606-12', '606-12'),  # Note that I've changed '606-04' to '606-12' to make it unique
)

    REGION_CHOICES = (
        ('Région Tanger-Tétouan-Al hoceima', 'Région Tanger-Tétouan-Al hoceima'),
        ('Région l\'Oriental', 'Région l\'Oriental'),
        ('Région Fès-Meknès', 'Région Fès-Meknès'),
        ('Région Rabat-Salé-Kénitra', 'Région Rabat-Salé-Kénitra'),
        ('Région Béni Mellal-Khénifra', 'Région Béni Mellal-Khénifra'),
        ('Région Casablanca-Settat', 'Région Casablanca-Settat'),
        # Ajoutez d'autres choix de région ici si nécessaire
    )

    LOCALITE_CHOICES = (
    # Région Tanger-Tétouan-Al hoceima
    ('Province d\'Alhoceima (zone A)', 'Province d\'Alhoceima (zone A)'),
    ('Province de chaouèn (zone B)', 'Province de chaouèn (zone B)'),
    ('Province d\'Ouezzane (zone B)', 'Province d\'Ouezzane (zone B)'),
    ('Province Tanger-Assillah (zone C)', 'Province Tanger-Assillah (zone C)'),
    ('Province de Fahs-Anjra (zone C)', 'Province de Fahs-Anjra (zone C)'),
    ('Province de Tétouan (zone C)', 'Province de Tétouan (zone C)'),
    ('Préfecture de M\'diq-Fnideq (zone C)', 'Préfecture de M\'diq-Fnideq (zone C)'),
    ('Province de Larache (zone C)', 'Province de Larache (zone C)'),
    # Région l'Oriental
    ('Province de Figuig (zone A)', 'Province de Figuig (zone A)'),
    ('Province de Gercif (zone B)', 'Province de Gercif (zone B)'),
    ('Province de Jerada (zone B)', 'Province de Jerada (zone B)'),
    ('Province de Berkane (zone B)', 'Province de Berkane (zone B)'),
    ('Province de Taourirt (zone B)', 'Province de Taourirt (zone B)'),
    ('Province de Nador (zone B)', 'Province de Nador (zone B)'),
    ('Province de Driouch (zone B)', 'Province de Driouch (zone B)'),
    ('Préfecture d\'Oujda-Angad (zone B)', 'Préfecture d\'Oujda-Angad (zone B)'),
    # Région Fès-Meknès
    ('Province de Boulemane (zone A)', 'Province de Boulemane (zone A)'),
    ('Province d\'Ifrane (zone A)', 'Province d\'Ifrane (zone A)'),
    ('Aderj,Ribate EL Kheir,lmouzzer Kandar,Ait Sebaa Lajrouf,lghezrane,Tafajight,Dar El Hamra (Province de Sefrou)(zone A)', 'Aderj,Ribate EL Kheir,lmouzzer Kandar,Ait Sebaa Lajrouf,lghezrane,Tafajight,Dar El Hamra (Province de Sefrou)(zone A)'),
    ('Province de Berkane (zone B)', 'Province de Berkane (zone B)'),
    ('Province de Taourirt (zone B)', 'Province de Taourirt (zone B)'),
    ('Province de Nador (zone B)', 'Province de Nador (zone B)'),
    ('Province de Driouch (zone B)', 'Province de Driouch (zone B)'),
    ('Préfecture d\'Oujda-Angad (zone B)', 'Préfecture d\'Oujda-Angad (zone B)'),
    # Région Rabat-Salé-Kénitra
    ('Préfecture de Rabat (zone C)', 'Préfecture de Rabat (zone C)'),
    ('Préfecture de Salé (zone C)', 'Préfecture de Salé (zone C)'),
    ('Préfecture de Skhirate-Témara (zone C)', 'Préfecture de Skhirate-Témara (zone C)'),
    ('Province de Khemisset (zone C)', 'Province de Khemisset (zone C)'),
    ('Province de Kenitra (zone C)', 'Province de Kenitra (zone C)'),
    ('Province de Sidi Kacem (zone C)', 'Province de Sidi Kacem (zone C)'),
    ('Province de Sidi Slimane (zone C)', 'Province de Sidi Slimane (zone C)'),
    # Région Béni Mellal-Kénitra
    ('Province d\'Azilal (zone A)', 'Province d\'Azilal (zone A)'),
    ('Province de Khénifra (zone A)', 'Province de Khénifra (zone A)'),
    ('Naour,Boutferda , Tizi Nisly,Aghbala,Foum El-Ansar,Tanougha,Taghzirt,Foum Oudi,Dir El Ksiba,Ait Oum El Bakht(zone B)', 'Naour,Boutferda , Tizi Nisly,Aghbala,Foum El-Ansar,Tanougha,Taghzirt,Foum Oudi,Dir El Ksiba,Ait Oum El Bakht(zone B)'),
    ('Province de Fquih Ben Salah (zone B)', 'Province de Fquih Ben Salah (zone B)'),
    ('Province de Khouribga (zone C)', 'Province de Khouribga (zone C)'),
    # Région Casablanca-Settat
    ('Préfecture de Casablanca (zone C)', 'Préfecture de Casablanca (zone C)'),
    ('Préfecture de Mohammedia (zone C)', 'Préfecture de Mohammedia (zone C)'),
    ('Province Nouaceur (zone C)', 'Province Nouaceur (zone C)'),
    ('Province Médiouna (zone C)', 'Province Médiouna (zone C)'),
    ('Province d\'El-Jadida (zone C)', 'Province d\'El-Jadida (zone C)'),
    ('Province de Sidi Bennour (zone C)', 'Province de Sidi Bennour (zone C)'),
    ('Province de Settat (zone C)', 'Province de Settat (zone C)'),
    ('Province de Benslimane (zone C)', 'Province de Benslimane (zone C)'),
    ('Province de Berrechid (zone C)', 'Province de Berrechid (zone C)'),
    )


    
    MUTUELLE_CHOICES = (
        ('MGPAP', 'MGPAP'),
        ('MGEN', 'MGEN'),
        ('DOUANES', 'DOUANES'),
        ('POLICE', 'POLICE'),
        ('F.AUX', 'F.AUX'),
        ('OMFAM', 'OMFAM'),
        # Ajoutez d'autres choix de mutuelle ici si nécessaire
    )
    
    categorie = models.CharField(max_length=120, choices=CATEGORIE_CHOICES)
    corps = models.CharField(max_length=120, choices=CORPS_CHOICES)
    cadre = models.CharField(max_length=120, choices=CADRE_CHOICES)
    grade = models.CharField(max_length=120, choices=GRADE_CHOICES)
    indice_echelon = models.CharField(max_length=120, choices=INDICE_ECHELON_CHOICES)
    region = models.CharField(max_length=120, choices=REGION_CHOICES,verbose_name='Région')
    localite = models.CharField(max_length=120, choices=LOCALITE_CHOICES,verbose_name='Localité')
    mutuelle = models.CharField(max_length=120, choices=MUTUELLE_CHOICES)
    est_marie = models.BooleanField(default=True,choices=[(True, 'Marié'), (False, 'Célibataire')],verbose_name='Situation Faimilial')
    nombre_enfants = models.IntegerField(choices=[(i, str(i)) for i in range(7)], default=0,verbose_name='Nombre d\'enfants')
    
    #Champ pour les résultats des calculs
    traitement_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    indemnite_residence = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_indemnites = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    allocation_medicale = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    indemnite_encadrement = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    indemnite_risque = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cotisation_mutuelle = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    secteur_mutualiste = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ccd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cotisations = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    impot_revenu = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #cotisation_cmr = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salaire_brut = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salaire_net_imposable = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_revenus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salaire_net = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def est_marie_ou_pas(self):
        if self.est_marie:
            return "Marié"
        else:
            return "Célibataire"

    def calculer_traitement_base(self):
        grille_indiciaire = {
    'Personnel de ministre de l\'enseignement supérieur': {
        'Corps des enseignants chercheurs de l\'enseignement supérieur': {
            'Professeur de l\'enseignement supérieur': {
                'Grade A': {
                    '760-01': 760,
                    '785-02': 785,
                    '810-03': 810,
                    '835-04': 835,
                },
                'Grade B': {
                    '860-01': 860,
                    '885-02': 885,
                    '915-03': 915,
                    '945-04': 945,
                },
                'Grade C': {
                    '975-01': 975,
                    '1005-02': 1005,
                    '1035-03': 1035,
                    '1065-04': 1065,
                    '1095-05': 1095,
                },
            },
            'Professeur habilite': {
                'Grade A': {
                    '580-01': 580,
                    '620-02': 620,
                    '660-03': 660,
                    '720-04': 720,
                },
                'Grade B': {
                    '779-01': 779,
                    '812-02': 812,
                    '840-03': 840,
                    '870-04': 870,
                },
                'Grade C': {
                    '900-01': 900,
                    '930-02': 930,
                    '960-03': 960,
                    '990-04': 990,
                    '1020-05': 1020,
                },
            },
            'Professeur assistant': {
                'Grade A': {
                    '509-01': 509,
                    '542-02': 542,
                    '574-03': 574,
                    '606-04': 606,
                },
                'Grade B': {
                    '639-01': 639,
                    '704-02': 704,
                    '746-03': 746,
                    '779-04': 779,
                },
                'Grade C': {
                    '812-01': 812,
                    '840-02': 840,
                    '870-03': 870,
                    '900-04': 900,
                },
                'Grade D': {
                    '930-01': 930,
                    '960-02': 960,
                    '990-03': 990,
                    '1020-04': 1020,
                },
            },
            'Professeur Agrégé': {
                'Grade A': {
                    '580-01': 580,
                    '620-02': 620,
                    '660-03': 660,
                    '720-04': 720,
                },
                'Grade B': {
                    '779-01': 779,
                    '812-02': 812,
                    '840-03': 840,
                    '870-04': 870,
                },
                'Grade C': {
                    '900-01': 900,
                    '930-02': 930,
                    '960-03': 960,
                    '990-04': 990,
                    '1020-05': 1020,
                },
            },
        },
        #Enseignant chercheurs de l'enseignement supérieur
        'Enseignant chercheurs de l\'enseignement supérieur': {

        },
        'Enseignants chercheurs de la médecine, la pharmacie et de médecine dentaire-NS': {
            'Professeur de l\'enseignement supérieur': {
                'Grade A': {
                    '760-01': 760,
                    '785-02': 785,
                    '810-03': 810,
                    '835-04': 835,
                },
                'Grade B': {
                    '860-01': 860,
                    '885-02': 885,
                    '915-03': 915,
                    '945-04': 945,
                },
                'Grade C': {
                    '975-01': 975,
                    '1005-02': 1005,
                    '1035-03': 1035,
                    '1065-04': 1065,
                    '1095-05': 1095,
                },
            },
            'Professeur assistant': {
                'Grade A': {
                    '509-01': 509,
                    '542-02': 542,
                    '574-03': 574,
                    '606-04': 606,
                },
                'Grade B': {
                    '639-01': 639,
                    '704-02': 704,
                    '746-03': 746,
                    '779-04': 779,
                },
                'Grade C': {
                    '812-01': 812,
                    '840-02': 840,
                    '870-03': 870,
                    '900-04': 900,
                },
                'Grade D': {
                    '930-01': 930,
                    '960-02': 960,
                    '990-03': 990,
                    '1020-04': 1020,
                },
            },
            'Professeur Agrégé': {
                'Grade A': {
                    '580-01': 580,
                    '620-02': 620,
                    '660-03': 660,
                    '720-04': 720,
                },
                'Grade B': {
                    '779-01': 779,
                    '812-02': 812,
                    '840-03': 840,
                    '870-04': 870,
                },
                'Grade C': {
                    '900-01': 900,
                    '930-02': 930,
                    '960-03': 960,
                    '990-04': 990,
                    '1020-05': 1020,
                },
            },
        },
    },
}
        print("**********************",self.corps,"***************************")
        print(len(grille_indiciaire[self.categorie][self.corps]))
        print("*************************************************")
        indice = grille_indiciaire[self.categorie][self.corps][self.cadre][self.grade][self.indice_echelon]
        point_indice = 100
        traitement_base = indice * point_indice
        return traitement_base
    
    def calculer_indemnite_residence(self):
        taux_indemnite = {
            'Région Tanger-Tétouan-Al hoceima': {
                'Province d\'Alhoceima (zone A)': 0.1,
                'Province de chaouèn (zone B)': 0.15,
                'Province d\'Ouezzane (zone B)': 0.15,
                'Province Tanger-Assillah (zone C)': 0.2,
                'Province de Fahs-Anjra (zone C)': 0.2,
                'Province de Tétouan (zone C)': 0.2,
                'Préfecture de M\'diq-Fnideq (zone C)': 0.2,
                'Province de Larache (zone C)': 0.2
            },
            # Ajoutez les autres régions et localités ici
        }
    
        taux = taux_indemnite.get(self.region, {}).get(self.localite, 0)
        traitement_base = self.calculer_traitement_base()
        indemnite_residence = taux * traitement_base
        return indemnite_residence


    def calculer_total_indemnites(self):
        allocation_medicale = self.allocation_medicale
        indemnite_encadrement = self.calculer_indemnite_encadrement()
        indemnite_risque = self.calculer_indemnite_risque()
        total_indemnites = allocation_medicale + indemnite_encadrement + indemnite_risque
        return total_indemnites

    def calculer_allocation_familiale(self, nombre_enfants):
        allocation_familiale = 0

        # Vérifiez si le nombre d'enfants est inférieur ou égal à 6
        if nombre_enfants <= 6:
            allocation_familiale = nombre_enfants #* taux_allocation_familiale

        # Retournez l'allocation familiale calculée
        return allocation_familiale


    def calculer_indemnite_encadrement(self, coefficient_encadrement):
        indemnite_encadrement = coefficient_encadrement #* taux_indemnite_encadrement
        return indemnite_encadrement

    def calculer_indemnite_recherche_appliquee(self, coefficient_recherche_appliquee):
        indemnite_recherche_appliquee = coefficient_recherche_appliquee #* taux_indemnite_recherche_appliquee
        return indemnite_recherche_appliquee

    def calculer_indemnite_risque(self, coefficient_risque):
        indemnite_risque = coefficient_risque #* taux_indemnite_risque
        return indemnite_risque


    def calculer_total_indemnites(self):
        allocation_medicale = self.calculer_allocation_medicale()
        indemnite_encadrement = self.calculer_indemnite_encadrement()
        indemnite_risque = self.calculer_indemnite_risque()

        total_indemnites = (
            allocation_medicale + indemnite_encadrement + indemnite_risque
        )

        return total_indemnites

    def calculer_total_mensuel_brut(self):
        traitement_base = self.calculer_traitement_base()
        indemnite_residence = self.calculer_indemnite_residence()
        allocation_medicale = self.calculer_allocation_medicale()
        indemnite_encadrement = self.calculer_indemnite_encadrement()
        indemnite_risque = self.calculer_indemnite_risque()

        total_mensuel_brut = (
            traitement_base + indemnite_residence +
            allocation_medicale + indemnite_encadrement + indemnite_risque
        )

        return total_mensuel_brut

    def calculer_cotisation_mutuelle(self):
        cotisation = 0
        if self.mutuelle == "MGPAP":
            cotisation = self.traitement_base * 0.03  # Exemple de calcul de cotisation pour MGPAP
        elif self.mutuelle == "MGEN":
            cotisation = self.traitement_base * 0.02  # Exemple de calcul de cotisation pour MGEN
        elif self.mutuelle == "DOUANES":
            cotisation = self.traitement_base * 0.01  # Exemple de calcul de cotisation pour DOUANES
        elif self.mutuelle == "POLICE":
            cotisation = self.traitement_base * 0.015  # Exemple de calcul de cotisation pour POLICE
        elif self.mutuelle == "F.AUX":
            cotisation = self.traitement_base * 0.025  # Exemple de calcul de cotisation pour F.AUX
        elif self.mutuelle == "OMFAM":
            cotisation = self.traitement_base * 0.02  # Exemple de calcul de cotisation pour OMFAM
        
        return cotisation

    def calculer_cotisation_amo(self):
        cotisation = 0
        if self.is_marie:
            cotisation = self.traitement_base * 0.04  # Exemple de calcul de cotisation AMO pour un professeur marié
        else:
            cotisation = self.traitement_base * 0.03  # Exemple de calcul de cotisation AMO pour un professeur non marié
        
        return cotisation

    def calculer_cotisation_sm(self):
        cotisation = self.traitement_base * 0.02  # Exemple de calcul de cotisation SM
        
        return cotisation

    def calculer_cotisation_ccd(self):
        cotisation = self.traitement_base * 0.01  # Exemple de calcul de cotisation CCD
        
        return cotisation

    def calculer_total_cotisations(self):
        cotisation_mutuelle = self.calculer_cotisation_mutuelle()
        cotisation_amo = self.calculer_cotisation_amo()
        cotisation_sm = self.calculer_cotisation_sm()
        cotisation_ccd = self.calculer_cotisation_ccd()

        total_cotisations = cotisation_mutuelle + cotisation_amo + cotisation_sm + cotisation_ccd
        return total_cotisations


    def calculer_impot_revenu(self, net_imposable):
        if net_imposable <= 30000:
           taux_imposition = 0
           constante_deduire = 0
        elif net_imposable <= 50000:
             taux_imposition = 10
             constante_deduire = 3000
        elif net_imposable <= 60000:
             taux_imposition = 20
             constante_deduire = 8000
        elif net_imposable <= 80000:
             taux_imposition = 30
             constante_deduire = 14000
        elif net_imposable <= 180000:
             taux_imposition = 34
             constante_deduire = 17200
        else:
             taux_imposition = 38
             constante_deduire = 24400

        nombre_deductions = self.calculer_nombre_deductions()
        impot_du = (net_imposable * taux_imposition / 100) - constante_deduire - (360 * nombre_deductions)
        return max(impot_du, 0)


    """def calculer_cotisation_cmr(self):
        traitement_base = self.calculer_traitement_base()

        # Calculer la cotisation CMR en fonction du traitement de base
        taux_cmr = 0.07  # Taux de cotisation CMR
        cotisation_cmr = traitement_base * taux_cmr

        return cotisation_cmr"""
    
    def calculer_salaire_brut(self):
        traitement_base = self.calculer_traitement_base()
        indemnite_residence = self.calculer_indemnite_residence()
        total_indemnites = self.calculer_total_indemnites()
        allocation_medicale = self.calculer_allocation_medicale()
        indemnite_encadrement = self.calculer_indemnite_encadrement()
        indemnite_risque = self.calculer_indemnite_risque()
        cotisation_mutuelle = self.calculer_cotisation_mutuelle()
        amo = self.calculer_assurance_maladie_obligatoire()
        secteur_mutualiste = self.calculer_secteur_mutualiste()
        ccd = self.calculer_caisse_complementaire_deces()
        #cotisation_cmr = self.calculer_cotisation_cmr()
        impot_revenu = self.calculer_impot_revenu()

        salaire_brut = (
            traitement_base
            + indemnite_residence
            + total_indemnites
            - allocation_medicale
            + indemnite_encadrement
            + indemnite_risque
            - cotisation_mutuelle
            - amo
            - secteur_mutualiste
            - ccd
            #- cotisation_cmr
            - impot_revenu
        )

        return salaire_brut


    def calculer_net_imposable(self, salaire_brut_imposable):
        if salaire_brut_imposable <= 30000:
           taux = 0
           forfait = 0
        elif salaire_brut_imposable <= 50000:
            taux = 10
            forfait = 30000
        elif salaire_brut_imposable <= 60000:
            taux = 20
            forfait = 8000
        elif salaire_brut_imposable <= 80000:
            taux = 30
            forfait = 14000
        elif salaire_brut_imposable <= 180000:
            taux = 34
            forfait = 17200
        else:
           taux = 38
           forfait = 24400

        net_imposable_modifie = (salaire_brut_imposable * (100 - taux) / 100) - forfait
        return max(net_imposable_modifie, 0)
    
    
    def calculer_total_revenus(self):
        salaire_brut = self.calculer_salaire_brut()
        indemnites_statutaires = self.calculer_total_indemnites_statutaires()
        allocation_medicale = self.calculer_allocation_medicale()
        indemnite_residence = self.calculer_indemnite_residence()

        total_revenus = salaire_brut + indemnites_statutaires + allocation_medicale + indemnite_residence

        return total_revenus

    def calculer_salaire_net(self):
        salaire_brut = self.calculer_salaire_brut()
        indemnites_statutaires = self.calculer_total_indemnites_statutaires()
        allocation_medicale = self.calculer_allocation_medicale()
        indemnite_residence = self.calculer_indemnite_residence()

        total_revenus = (
            salaire_brut + indemnites_statutaires + allocation_medicale + indemnite_residence
        )

        #cotisation_cmr = self.calculer_cotisation_cmr(salaire_brut)
        impot_revenu = self.calculer_impot_revenu(total_revenus)

        salaire_net = total_revenus - impot_revenu#cotisation_cmr 

        return salaire_net
    def __str__(self):
        return self.name

    
    def calculer_frais_professionnels(self, salaire_brut_imposable):
        date_plafond_30000 = datetime(2010, 1, 1)
        salaire_plafond_78000 = 78000

        if salaire_brut_imposable <= salaire_plafond_78000:
           frais_professionnels = min(0.3 * salaire_brut_imposable, 35000)
        else:
           frais_professionnels = min(0.25 * salaire_brut_imposable, 35000)

        if date.today() >= date_plafond_30000:
           frais_professionnels_annuel = min(0.2 * salaire_brut_imposable, 30000)
        else:
           frais_professionnels_annuel = 0

        return max(frais_professionnels, frais_professionnels_annuel)


'''class MyAccountManager(BaseUserManager):
    def create_user(self, user_id,is_employee=True,usernmane="",email="xyz@gmail.",is_employer=False,password=None):
        if not user_id:
            raise ValueError('Users must have a userID')

        user = self.model(
            email = self.normalize_email(email),
            usernmane = usernmane,
            user_id=user_id,
            is_employee = is_employee,
            is_employer = is_employer,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, is_employee=False, is_employer=False,usernmane="",email="xyz@gmail.", password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            usernmane = usernmane,
            user_id=user_id,
            is_employee = False,
            is_employer = False,
            password=password,
        )
        user.email=email
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    user_id = models.IntegerField(verbose_name="user_id",  unique=True, primary_key=True)
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    email = models.EmailField(blank=True,null=True,verbose_name='email')
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)


    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['is_employer','is_employee']

    objects = MyAccountManager()

    def __str__(self):
        return str(self.user_id)

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True'''

class Rubrique(models.Model):
    libele_rubrique = models.CharField(max_length=255)
    montant_mensuel = models.DecimalField(max_digits=10, decimal_places=2)


################################################################

class ListeGrade(models.Model):
    codecate = models.IntegerField(primary_key=True)
    libecate = models.CharField(max_length=255)
    codecorp = models.IntegerField()
    codecadr = models.IntegerField()
    idengrad = models.IntegerField(default=0)
    codegrad = models.IntegerField()
    libegrad = models.CharField(max_length=255)
    codecomp = models.IntegerField()
    codfamgr = models.CharField(max_length=10)
    echelle = models.IntegerField()
    echelon = models.IntegerField()
    poinindi = models.IntegerField()   

    def __str__(self):
        return self.libecate

    class Meta:
        db_table = 'liste_grade'



class ListeFamilleGrade(models.Model):
    codfamgr = models.CharField(max_length=10, primary_key=True)
    libfamgr = models.CharField(max_length=255)
    echelle = models.IntegerField()
    dateeffe = models.DateField()
    
    def __str__(self):
        return self.libfamgr
    
    class Meta:
        db_table = 'liste_famille_grade'



class ListeGradeFamilleGrade(models.Model):
    idengrad = models.IntegerField()
    codfamgr = models.CharField(max_length=10)

    class Meta:
        db_table = 'liste_grade_famille_grade'
        unique_together = ('idengrad', 'codfamgr')




class RubDroitProfEnsSec2Gr(models.Model):
    idendroi = models.IntegerField(primary_key=True)
    idengrad = models.IntegerField()
    coderubr = models.CharField(max_length=255, db_collation='pg_catalog.default')
    libegrad = models.CharField(max_length=255, db_collation='pg_catalog.default')
    liberubr = models.CharField(max_length=255, db_collation='pg_catalog.default')
    naturubr = models.CharField(max_length=255, db_collation='pg_catalog.default')

    def __str__(self):
        return self.liberubr

    class Meta:
        db_table = 'rub_droit_prof_ens_sec_2_gr'



class SitPaieProfEnsSec2Gr(models.Model):
    idendroi = models.CharField(max_length=255, primary_key=True, db_collation='pg_catalog.default')
    idengrad = models.IntegerField()
    idencomb = models.IntegerField()
    codfamgr = models.CharField(max_length=10)
    echelon = models.IntegerField()
    idendepa = models.IntegerField()
    codezone = models.CharField(max_length=10)
    coderubr = models.CharField(max_length=255, db_collation='pg_catalog.default')
    liberubr = models.CharField(max_length=255)
    montoctr = models.DecimalField(max_digits=15, decimal_places=2)
    typeoctr = models.CharField(max_length=50)
    perioctr = models.CharField(max_length=50)
    
    def __str__(self):
        return self.montoctr

    class Meta:
        db_table = 'sit_paie_prof_ens_sec_2_gr'
