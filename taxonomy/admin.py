from django.contrib import admin
from taxonomy.models import Genus, Species, Variety, UserTaxonomySettings

# Register your models here.
admin.site.register(Genus)
admin.site.register(Species)
admin.site.register(Variety)
admin.site.register(UserTaxonomySettings)

