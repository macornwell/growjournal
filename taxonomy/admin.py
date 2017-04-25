from django.contrib import admin
from taxonomy.models import Genus, Species, Cultivar, UserTaxonomySettings, SiteInventory, LifeForm, Rootstock, Kingdom

# Register your models here.
admin.site.register(Genus)
admin.site.register(SiteInventory)
admin.site.register(Species)
admin.site.register(Cultivar)
admin.site.register(UserTaxonomySettings)
admin.site.register(LifeForm)
admin.site.register(Rootstock)
admin.site.register(Kingdom)

