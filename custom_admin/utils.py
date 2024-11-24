def get_google_oauth_keys():
    """
    Retrieve Google OAuth keys from the database.
    """
    from custom_admin.models import OAuthKey
    try:
        key = OAuthKey.objects.get(provider="google")
        return {
            "client_id": key.client_id,
            "client_secret": key.client_secret,
        }
    except OAuthKey.DoesNotExist:
        return {
            "client_id": "",
            "client_secret": "",
        }
