from django.contrib import admin
from WebAppServicios.models import servicio

# Register your models here.


class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("titulo", "contenido", "imagen", "created", "updated")
    search_fields = ("titulo", "created", "updated")
    date_hierarchy = "updated"


admin.site.register(servicio, ServiciosAdmin)
