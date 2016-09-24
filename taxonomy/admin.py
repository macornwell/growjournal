from django.contrib import admin
from taxonomy.models import Genus, Species, Variety, UserTaxonomySettings, SiteInventory, LifeForm, Rootstock, Kingdom

# Register your models here.
admin.site.register(Genus)
admin.site.register(SiteInventory)
admin.site.register(Species)
admin.site.register(Variety)
admin.site.register(UserTaxonomySettings)
admin.site.register(LifeForm)
admin.site.register(Rootstock)
admin.site.register(Kingdom)

