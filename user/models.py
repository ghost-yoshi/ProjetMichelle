from django.db import models

class Locataire(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    telephone = models.IntegerField(max_length=10)
    email = models.EmailField()
    mot_de_passe = models.IntegerField()
    photo_profil = models.CharField()
    date_creation = models.DateField() 

    def __str__(self):
        return self.email
    
class Proprietaire(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    telephone = models.IntegerField(max_length=10)
    email = models.EmailField()
    mot_de_passe = models.IntegerField()
    photo_profil = models.CharField()
    date_creation = models.DateField() 
    type_proprietaire = models.CharField(max_length=20)
    statut_compte = models.IntegerField()

    def __str__(self):
        return self.nom 
    

    
# Create your models here.
