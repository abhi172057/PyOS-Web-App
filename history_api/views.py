from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from history_api.services.history_service import HistoryService


# =========================
# HISTORY API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):

    logs = HistoryService.get_user_history(request.user)

    return Response([
        {
            "id": log.id,
            "user": log.user.username,
            "command": log.command,
            "timestamp": log.executed_at
        }
        for log in logs
    ])


# =========================
# FILTER HISTORY API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_history(request):

    keyword = request.GET.get("q")

    if not keyword:
        return Response({"error": "Query required"}, status=400)

    logs = HistoryService.filter_history(request.user, keyword)

    return Response([
        {
            "id": log.id,
            "user": log.user.username,
            "command": log.command,
            "timestamp": log.executed_at,
        }
        for log in logs
    ])