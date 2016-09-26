from core.models import Site, UserCoreSettings


def get_user_core_settings(user):
    return UserCoreSettings.objects.get_or_create(user=user)[0]


def get_active_site(user):
    if user.is_authenticated():
        settings = get_user_core_settings(user)
        return settings.active_site
    else:
        return None

