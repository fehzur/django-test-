from django.db import models

class Reservation(models.Model):
    nom = models.CharField(max_length=255)
    date_reservation = models.DateTimeField(auto_now_add=True)
    # Ajoutez d'autres champs selon vos besoins
