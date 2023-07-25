from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')  # Campos a serem exibidos na lista

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'observacao')  # Campos a serem exibidos na lista

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('brinco', 'sexo', 'raca', 'tipo', 'pasto', 'observacoes')  # Campos a serem exibidos na lista



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Medicamento)
admin.site.register(Origem)
admin.site.register(Raca)
admin.site.register(StatusAnimal)
admin.site.register(CausaMorte)
admin.site.register(Pasto)
admin.site.register(ClassificacaoSanidade)
admin.site.register(Tipo)
admin.site.register(Despesa)
admin.site.register(Lote)
admin.site.register(Caracteristica)