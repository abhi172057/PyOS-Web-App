from django.urls import path
from .views import recycle_bin, restore_item, delete_permanently

urlpatterns = [
    path('', recycle_bin),
    path('restore/<int:item_id>/', restore_item),
    path('delete/<int:item_id>/', delete_permanently),
]