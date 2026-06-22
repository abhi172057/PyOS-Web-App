from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Root API view (optional but professional)
def home(request):
    return JsonResponse({
        "message": "PyOS Backend Running 🚀",
        "status": "success"
    })


urlpatterns = [
    # Home route
    path('', home),
    path('home/', home),

    # Admin panel
    path('admin/', admin.site.urls),

    # ======================
    # Authentication (JWT)
    # ======================
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ======================
    # PyOS APIs
    # ======================
    path('api/users/', include('users_api.urls')),
    path('api/filesystem/', include('filesystem_api.urls')),
    path('api/history/', include('history_api.urls')),
    path('api/logs/', include('logs_api.urls')),
    path('api/recyclebin/', include('recyclebin_api.urls')),
]