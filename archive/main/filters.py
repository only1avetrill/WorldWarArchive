import django_filters
from django.forms import TextInput
from django_filters import DateFilter, CharFilter
from .models import *

class DocsFilter(django_filters.FilterSet):
    first_year = CharFilter(field_name='year', lookup_expr='gte')
    second_year = CharFilter(field_name='year', lookup_expr='lte')
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Document
        fields = ['first_year', 'second_year', 'title', 'category', 'country']


