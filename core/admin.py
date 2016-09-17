from django.contrib import admin
from core.models import Project, WebsiteFeedback, Site

admin.site.register(Site)
admin.site.register(Project)
admin.site.register(WebsiteFeedback)