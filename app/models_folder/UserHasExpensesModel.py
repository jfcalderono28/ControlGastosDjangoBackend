from ..models_folder import models

class UserHasExpensesModel(models.Model):

    name_expense = models.models.CharField( max_length=50)
    expense = models.models.models.models.IntegerField()
    id_poket = models.ForeignKey("app.poketModel", verbose_name=("bolsillo"), on_delete=models.CASCADE)
    id_expense_type = models.ForeignKey("app.expenseType", verbose_name=("Tipo de gasto"), on_delete=models.CASCADE)
    id_user = models.ForeignKey("app.userModel", verbose_name=("id usuario"), on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.name_expense
    
    class Meta: 
        db_table = 'expense_has_type'

 