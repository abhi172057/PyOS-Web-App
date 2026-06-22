from django.urls import path
from .views import register_user, me, list_users, update_user

urlpatterns = [
    path('register/', register_user),
    path('me/', me),
    path('list/', list_users),
    path('update/', update_user),
]