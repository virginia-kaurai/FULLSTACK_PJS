from django.contrib import admin
from . import models

@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'created_at')
    search_fields = ('name', 'faculty__name')
  
    ordering = ('-created_at',)

    admin.site.register(models.Faculty)
@admin.register(models.ClassDetail)
class ClassDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name__name', 'description')
    ordering = ('-created_at',)

    
    
  