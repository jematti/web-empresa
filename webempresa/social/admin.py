from django.contrib import admin
from .models import Link    

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name', 'created_at', 'updated_at')  # Todos los campos de solo lectura
        else:
            return ('created_at', 'updated_at')  # Solo fechas de solo lectura

admin.site.register(Link, LinkAdmin)
