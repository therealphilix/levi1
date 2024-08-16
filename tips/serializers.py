from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField
from .models import Tip, ProgrammingLanguage

class ProgLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ['id', 'title']

class TipSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Tip
        fields = ['id', 'title', 'description', 'created_at', 'programming_language', 'tags']

