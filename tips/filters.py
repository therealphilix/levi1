from django_filters.rest_framework import FilterSet
from .models import Tip

class TipFilter(FilterSet):
    class Meta:
        model = Tip
        fields = {
            'programming_language_id': ['exact']
        }