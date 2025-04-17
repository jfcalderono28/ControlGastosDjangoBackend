from ..serializer_folder import serializers
from ..models_folder import UserHasExpensesModel

class UserHasExpensesSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = UserHasExpensesModel
        fields = ('expense','id_user','id_currency','id_poket','id_expense_type',)