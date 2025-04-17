from ..models_folder import models

class ExpenseTypeModel(models.Model):

    name_type = models.CharField(max_length=150)
    id_expense_category = models.ForeignKey("app.expenseCategory", verbose_name=("Tipo tiene categoria"), on_delete=models.CASCADE)
    id_user = models.ForeignKey("app.userModel", verbose_name=("id usuario"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)   
    update_created = models.DateTimeField(auto_now=True)  
    

    def __str__(self):
        return self.name_category
    
    class Meta: 
        db_table = 'expense_has_type'

 