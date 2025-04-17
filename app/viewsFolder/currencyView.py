# viewsFolder/userView.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



#Serializer
from ..serializer_folder.CurrencySerializer import CurrencySerializer

#Models
from ..models_folder.CurrencyModel import CurrencyModel


@api_view(['POST'])
def RegisterCurrencyView(request):  
    serializer =  CurrencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Moneda creada exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
