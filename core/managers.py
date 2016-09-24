from django.db import models

class NameAscendingOrderManager(models.Manager):
    def get_queryset(self):
        return super(NameAscendingOrderManager, self).get_queryset().order_by('name')

class SiteManager(models.Manager):
    def get_queryset(self):
        return super(SiteManager, self).get_queryset().filter(deleted=False)