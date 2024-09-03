from django.db import models

class Material(models.Model):
    nazev = models.CharField(max_length=200)
    cena = models.CharField(max_length=200)
    sklad = models.CharField(max_length=200)

    def __str__(self):
        return self.nazev


