from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services.log_service import LogService


# =========================
# GET ALL LOGS (ADMIN VIEW)
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logs(request):
    logs = LogService.get_logs()

    if not logs:
        return Response({"message": "No logs found"}, status=200)

    return Response([
        {
            "id": log.id,
            "action": log.action,
            "description": log.description,
            "user": log.user.username if log.user else None,
            "timestamp": log.created_at
        }
        for log in logs
    ])