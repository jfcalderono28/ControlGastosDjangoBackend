from django.db import models

class CurrencyModel(models.Model):
    name_currency = models.CharField(max_length=150, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)   # se fija al crear
    update_created = models.DateTimeField(auto_now=True)     # se actualiza en cada save()

    def __str__(self):
        return self.name_currency  

    class Meta:
        db_table = 'currency'
