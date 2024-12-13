from django.db import models

class Cabida(models.Model):
    lado_a = models.FloatField()
    lado_b = models.FloatField()
    lado_x = models.FloatField()
    lado_y = models.FloatField()
    resultado = models.IntegerField(null=True, blank=True)
