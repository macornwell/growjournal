from core.models import Site, UserCoreSettings

def get_user_core_settings(user):
    return UserCoreSettings.objects.get_or_create(user=user)[0]

