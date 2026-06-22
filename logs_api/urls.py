from django.urls import path
from .views import logs

urlpatterns = [
    # 📊 Get all system logs
    path('all/', logs, name='logs-list'),
]