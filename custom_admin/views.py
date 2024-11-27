from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from allauth.account.views import LoginView
from allauth.socialaccount.models import SocialApp
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse

class CustomLoginView(LoginView):
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        
        if self.request.user.is_superuser:
            return reverse('superadmin') 
        else:
            return reverse('task-list')

def superadmin(request):
    if not request.user.is_superuser:
        return redirect('task-list')
    
    social_apps = SocialApp.objects.all()

    context = {
        'social_apps': social_apps
    }
    return render(request, 'superadmin.html', context)



@user_passes_test(lambda u: u.is_superuser)
def add_update_socialapp(request, pk=None):
    if pk:
        social_app = get_object_or_404(SocialApp, pk=pk)
        action = "Update"
    else:
        social_app = SocialApp()
        action = "Add"

    if request.method == "POST":
        social_app.name = request.POST.get("name")
        social_app.client_id = request.POST.get("client_id")
        social_app.secret = request.POST.get("secret")
        social_app.provider = request.POST.get("provider")
        social_app.save()
        messages.success(request, f"{action} successful!")
        return redirect("superadmin")

    return render(request, "add_update_socialapp.html", {"social_app": social_app, "action": action})


@user_passes_test(lambda u: u.is_superuser)
def delete_socialapp(request, pk):
    if request.method == "POST":
        social_app = get_object_or_404(SocialApp, pk=pk)
        social_app.delete()
        return JsonResponse({"success": True, "message": "Application deleted successfully!"})
    return JsonResponse({"success": False, "message": "Invalid request"})

@user_passes_test(lambda u: u.is_superuser)
def send_invitation_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = "You're Invited!"
        message = "<h1>Welcome!</h1><p>You have been invited to join our platform.</p>"
        from_email = 'your_email@gmail.com'

        try:
            email_message = EmailMessage(subject, message, from_email, [email])
            email_message.content_subtype = 'html'  # Set the email content type to HTML
            email_message.send()
            return HttpResponse("HTML Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")
