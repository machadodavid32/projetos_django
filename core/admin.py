from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente  # Aqui estamos importando os produtos do arquivo models


class ProdutoAdmin(admin.ModelAdmin):  # Aqui estamos colocando coluna de nome, preço e estoque no campo produtos no site
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

