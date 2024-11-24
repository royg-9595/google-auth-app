from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import OAuthKeyForm
from .models import OAuthKey

@user_passes_test(lambda u: u.is_superuser)
def manage_oauth_keys(request):
    key = OAuthKey.objects.filter(provider="google").first()
    if request.method == "POST":
        form = OAuthKeyForm(request.POST, instance=key)
        if form.is_valid():
            form.save()
            return redirect("manage-oauth-keys")
    else:
        form = OAuthKeyForm(instance=key)
    return render(request, "tasks/manage_oauth_keys.html", {"form": form})

