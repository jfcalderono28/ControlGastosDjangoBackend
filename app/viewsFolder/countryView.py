# viewsFolder/countryView.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


# Serializer
from ..serializer_folder.CountrySerializer import CountrySerializer
from ..serializer_folder.CurrencySerializer import CurrencySerializer
from ..serializer_folder.CountriesHasCurrenciesSerializer import CountriesHasCurrenciesSerializer

# Models
from ..models_folder.CountryModel import CountryModel
from ..models_folder.CurrencyModel import CurrencyModel
from ..models_folder.CountriesHasCurrenciesModel import CountriesHasCurrenciesModel


'''@api_view(['POST'])
def RegisterCountryView(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "País creado exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SearchCountryView(request):
    query = request.GET.get('query', '')

    countries = CountryModel.objects.filter(
        Q(name_country__icontains=query)
    )
    ids = request.GET.getlist('ids[]')
    if ids:
        countries = countries.filter(id__in=ids)

    currency_links = CountriesHasCurrenciesModel.objects.filter(
        id_country__in=countries
    ).select_related('id_currency', 'id_country')

    country_currency_map = {}
    for link in currency_links:
        country_id = link.id_country.id
        currency = link.id_currency
        if country_id not in country_currency_map:
            country_currency_map[country_id] = []
        country_currency_map[country_id].append({
            "id": currency.id,
            "name": currency.name_currency,
            
        })

    # Ordenar las monedas por nombre dentro de cada país
    for currency_list in country_currency_map.values():
        currency_list.sort(key=lambda x: x['name'].lower())

    result = []
    for country in countries:
        result.append({
            "id": country.id,
            "name": country.name_country,
            "currencies": country_currency_map.get(country.id, [])
        })

    return Response(result, status=status.HTTP_200_OK)
