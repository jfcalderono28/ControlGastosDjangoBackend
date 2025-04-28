from django.urls import path
from .viewsFolder import userView
from .viewsFolder import countryView
from .viewsFolder import currencyView
from .viewsFolder import CountriesHasCurrenciesView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # user
    path('user/register/', userView.RegisterUserView),
    path('user/info/', userView.InfoUserView),
    path('user/search/', userView.SearchUserView),
    path('user/update/<int:user_id>/', userView.UpdateUserView),


    # user-country
    # path('country/register/', countryView.RegisterCountryView),
    path('country/search/', countryView.SearchCountryView),

    path('user/country/add/<int:user_id>', userView.AddCountriesToUserView),

    # user-currency
    path('currency/search/', currencyView.SearchCurrencyView),
    path('currency/register/', currencyView.RegisterCurrencyView),
    path('currency/update/<int:currency_id>/', currencyView.UpdateCurrencyView),

    # country-currency
    path('country/register/',
         CountriesHasCurrenciesView.RegisterCountryView),
    path('country/update/',
         CountriesHasCurrenciesView.UpdateCountryView),
    path('country/list/currency/<country_id>',
         CountriesHasCurrenciesView.getCurrenciesOfCountry),

    # auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
