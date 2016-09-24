from core.models import Site
from core.services import get_user_core_settings


def user_sites(request):
    user = request.user
    list = []
    if user.is_authenticated():
        settings = get_user_core_settings(user)
        sites = Site.objects.filter(user=user)
        active = settings.active_site
        if active:
            list.append(active)
        for site in sites:
            if site != active:
                list.append(site)
    return {'user_sites': list}

