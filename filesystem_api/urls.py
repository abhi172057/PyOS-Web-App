from django.urls import path
from .views import (
    create_directory,
    create_file,
    list_directory,
    search,
    delete_file,
    delete_directory,
    move_file,
    move_directory
)

urlpatterns = [
    path('mkdir/', create_directory),
    path('touch/', create_file),
    path('ls/<int:directory_id>/', list_directory),
    path("search/", search), 
    path('delete/<int:file_id>/', delete_file),
    path('move-file/', move_file),
    path('move-directory/', move_directory),
    path(
    'delete-directory/<int:directory_id>/',
    delete_directory
),
]