# viewsFolder/userView.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



#Serializer
from ..serializer_folder.CountrySerializer import CountrySerializer

#Models
from ..models_folder.CountryModel import CountryModel


@api_view(['POST'])
def RegisterCountryView(request):  
    serializer =  CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "País creado exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
