from ..models_folder import models

class ExpenseCategoryModel(models.Model):

    name_category = models.CharField(max_length=150)
    id_user = models.ForeignKey("app.userModel", verbose_name=("id usuario"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)   
    update_created = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.name_category
    
    class Meta: 
        db_table = 'expense_category'

