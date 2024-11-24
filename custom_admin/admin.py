from django.contrib import admin
from .models import OAuthKey

@admin.register(OAuthKey)
class OAuthKeyAdmin(admin.ModelAdmin):
    list_display = ("provider", "client_id")
