from django.contrib import admin
from .models import Tip, ProgrammingLanguage as Program
# Register your models here.

@admin.register(Tip)
class TipsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass
