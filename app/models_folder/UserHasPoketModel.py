from ..models_folder import models

class Poket(models.Model):

    name = models.CharField(max_length=150)
    id_user = models.ForeignKey("app.userModel", verbose_name=("id usuario"), on_delete=models.CASCADE)
    id_status   = models.models.SmallIntegerField()
    total = models.models.BigIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)   
    update_created = models.DateTimeField(auto_now=True)  




    def __str__(self):
        return self.name
    
    class Meta: 
            db_table = 'user_has_pokets'