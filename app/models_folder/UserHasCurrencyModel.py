from django.db import models

class UserHasCurrencyModel(models.Model):
    
    date_created = models.DateTimeField(auto_now_add=True)   # se fija al crear
    update_created = models.DateTimeField(auto_now=True)     # se actualiza en cada save()
    id_user = models.ForeignKey("app.userModel", verbose_name=("id usuario"), on_delete=models.CASCADE)
    id_Currency = models.ForeignKey("app.CurrencyModel", verbose_name=("currency"), on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.id_user} - {self.id_Currency}"

    class Meta:
        db_table = 'user_has_currency'
