from django.urls import path
from notifications import views  # Make sure this import is correct

urlpatterns = [
    path('notifications/', views.send_notification),
    path('users/<int:id>/notifications/', views.get_user_notifications),
]