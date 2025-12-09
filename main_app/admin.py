from django.contrib import admin

from .models import Category, Technique


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'category', 'created_at')
    list_filter = ('category', 'user')
    search_fields = ('name', 'description')
