from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class ProgrammingLanguage(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Tip(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self) -> str:
        return self.title
    


