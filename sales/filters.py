import django_filters as filters
from .models import Client


class ClientStatisticsFilter(filters.FilterSet):
    month = filters.NumberFilter(field_name='order__date', lookup_expr='month')
    year = filters.NumberFilter(field_name='order__date', lookup_expr='year')

    class Meta:
        model = Client
        fields = ['month', 'year', ]
