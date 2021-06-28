from django.db import models


# Create your models here.


class Stock(models.Model):
    Codigo = models.CharField(max_length=6)
    Preço = models.DecimalField(max_digits=9, decimal_places=2)
    Quantidade = models.IntegerField()
    Data = models.DateField()

    def __str__(self):
        return self.Codigo
