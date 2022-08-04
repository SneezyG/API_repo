from django.contrib import admin
from .models import Element, ChemicalConstant, PhysicalConstant, Particle

# Register your models here.


admin.site.register(Element)
admin.site.register(ChemicalConstant)
admin.site.register(PhysicalConstant)
admin.site.register(Particle)

class AuthorAdmin(admin.ModelAdmin):
  pass