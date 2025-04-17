from django.db import models

class CountryModel(models.Model):
    name_country = models.CharField(max_length=150, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)   # se fija al crear
    update_created = models.DateTimeField(auto_now=True)     # se actualiza en cada save()

    def __str__(self):
        return self.name_country  

    class Meta:
        db_table = 'country'
