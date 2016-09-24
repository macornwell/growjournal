from taxonomy.models import UserTaxonomySettings

def use_latin_names(request):
    useLatin = False
    if request.user.is_authenticated:
        settings = UserTaxonomySettings.objects.get_settings(request.user)
        useLatin = settings.use_latin_name
    return {'use_latin': useLatin}
