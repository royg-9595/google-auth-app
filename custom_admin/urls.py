from django.urls import path
from . import views
from .views import add_update_socialapp, delete_socialapp, send_invitation_email

urlpatterns = [
    path("accounts/login/", views.CustomLoginView.as_view(), name="account_login"),
    path("superadmin/", views.superadmin, name="superadmin"),
    path("socialapp/add/", add_update_socialapp, name="add-socialapp"),
    path("socialapp/<int:pk>/edit/", add_update_socialapp, name="update-socialapp"),
    path("socialapp/<int:pk>/delete/", delete_socialapp, name="delete-socialapp"),
    path('send-invite/', send_invitation_email, name='send-invite'),
]