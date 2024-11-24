from django.db import models

class OAuthKey(models.Model):
    provider = models.CharField(max_length=50, unique=True)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.provider} OAuth Key"
