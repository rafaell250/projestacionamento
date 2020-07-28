from django.contrib import admin
from .models import (
    Pessoa, 
    Marca,
    Veiculo, 
    Parametros, 
    MovRotativo,
    Mensalista,
    Movmensalista,
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'chekin', 
        'chekout', 
        'valor_hora',
        'horas_total', 
        'veiculo',
        'total', 
        'situacao',
    )


class MovmensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista',
        'dt_pgt',
        'total',
    )


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(Movmensalista, MovmensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
