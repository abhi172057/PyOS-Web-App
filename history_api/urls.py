from django.urls import path
from .views import history, filter_history

urlpatterns = [
    path('', history),
    path('filter/', filter_history),
]