from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recyclebin_api.services.recycle_service import RecycleService


# =========================
# LIST RECYCLE BIN
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recycle_bin(request):

    items = RecycleService.get_bin(request.user)

    return Response([
        {
            "id": item.id,
            "name": item.item_name,
            "type": item.item_type,
            "deleted_at": item.deleted_at
        }
        for item in items
    ])


# =========================
# RESTORE ITEM
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def restore_item(request, item_id):

    success = RecycleService.restore_item(
        item_id,
        request.user
    )

    if success:
        return Response({
            "message": "Item restored successfully"
        })

    return Response({
        "error": "File already exists or item not found"
    }, status=400)

# =========================
# PERMANENT DELETE
# =========================
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_permanently(request, item_id):

    success = RecycleService.permanent_delete(item_id, request.user)

    if not success:
        return Response({"error": "Item not found"}, status=404)

    return Response({"message": "Item permanently deleted"})