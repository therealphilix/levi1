from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Tip, ProgrammingLanguage
from .serializers import TipSerializer, ProgLanguageSerializer
from .pagination import DefaultPagination
from .filters import TipFilter
# Create your views here.

class TipViewSet(ModelViewSet):
    queryset = Tip.objects.select_related('programming_language').all()
    serializer_class = TipSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = TipFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'tags__name']
    

class ProgrammingLanguageViewSet(ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgLanguageSerializer 