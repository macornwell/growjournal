from django.contrib import admin
from core.models import Project, WebsiteFeedback, Site


class SiteAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    def get_queryset(self, request):
        qs = super(SiteAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SiteAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            self.exclude = ('user', 'site_users',)
        form.user = request.user
        return form

admin.site.register(Site, SiteAdmin)
admin.site.register(Project)
admin.site.register(WebsiteFeedback)