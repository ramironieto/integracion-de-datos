from django.contrib import admin
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
   list_display= ['titulo','tipo', 'barrio', 'precio', 'gastos_comunes']


admin.site.register(Property, PropertyAdmin)