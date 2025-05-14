from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    # Responsável por dizer quais as colunas que serão exibidas na tela de admin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    # Responsável por qual campo será possível pesquisar
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    # Responsável por dizer quais as colunas que serão exibidas na tela de admin
    list_display = ('name',)
    # Responsável por qual campo será possível pesquisar
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)