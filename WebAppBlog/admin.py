from django.contrib import admin
from WebAppBlog.models import categoria, post

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "created", "updated")
    search_fields = ("nombre", "created", "updated")
    date_hierarchy = "updated"


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("titulo", "contenido", "imagen", "autor",
                    "created", "updated")
    search_fields = ("titulo", "autor", "created", "updated")
    date_hierarchy = "updated"


admin.site.register(categoria, CategoriaAdmin)
admin.site.register(post, PostAdmin)
