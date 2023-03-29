from django.contrib import admin
from temas.models import Tema

class TemaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Tema, TemaAdmin)