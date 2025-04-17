from django.db import models
from .CountryModel import CountryModel
from .CurrencyModel import CurrencyModel

class CountriesHasCurrenciesModel(models.Model):
    id_currency = models.ForeignKey(
        CurrencyModel,
        on_delete=models.CASCADE,
        db_column='id_currency',
        verbose_name="id currency"
    )
    id_country = models.ForeignKey(
        CountryModel,
        on_delete=models.CASCADE,
        db_column='id_country',
        verbose_name="id country"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    update_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id_currency} - {self.id_country}"


    class Meta:
        db_table = 'countries_has_currencies'
        unique_together = ('id_currency', 'id_country')
