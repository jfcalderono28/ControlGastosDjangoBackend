from django.db import models
from .UserModel import UserModel
from .CountryModel import CountryModel

class UserHasCountriesModel(models.Model):
    id_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        db_column='id_user',
        verbose_name="id usuario"
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
        return f"{self.id_user} - {self.id_country}"

    class Meta:
        db_table = 'user_has_countries'
        unique_together = ('id_user', 'id_country')
