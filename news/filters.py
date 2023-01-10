from django.forms import DateInput
from django_filters import FilterSet, DateFilter

from .models import *


class NewFilter(FilterSet):
    date = DateFilter(
        field_name='date_pub',
        lookup_expr='gt',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )
    date.field.error_messages = {'invalid': 'Enter date in format DD.MM.YYYY. Example: 06.09.2022'}
    date.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}


class Meta:
    model = New
    fields = {
        'name',
        'category',
    }
