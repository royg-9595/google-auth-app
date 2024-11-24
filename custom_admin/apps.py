from django.apps import AppConfig
from django.conf import settings
from custom_admin.utils import get_google_oauth_keys

class CustomAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_admin'
    
    # def ready(self):
    #     # Populate SOCIALACCOUNT_PROVIDERS after the app registry is ready
    #     oauth_keys = get_google_oauth_keys()
    #     settings.SOCIALACCOUNT_PROVIDERS = {
    #         "google": {
    #             "APP": oauth_keys,
    #         }
    #     }
