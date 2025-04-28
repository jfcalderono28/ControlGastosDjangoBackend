# viewsFolder/userView.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Serializer
from ..serializer_folder.CurrencySerializer import CurrencySerializer

# Models
from ..models_folder.CurrencyModel import CurrencyModel


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SearchCurrencyView(request):
    query = request.GET.get('query', '')

    # Suponiendo que haces un filtrado por nombre o correo
    currencies = CurrencyModel.objects.filter(
        Q(name_currency__icontains=query) 
    )

    result = []
    for currency in currencies:
        result.append({
            "id": currency.id,
            "name_currency": currency.name_currency,
            
        })

    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def RegisterCurrencyView(request):
    serializer = CurrencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Moneda creada exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def UpdateCurrencyView(request, currency_id):
    try:
        user = CurrencyModel.objects.get(id=currency_id)
    except CurrencyModel.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CurrencySerializer(
        user, data=request.data, partial=True)  # actualiza parcialmente
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Currency actualizado correctamente"}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
