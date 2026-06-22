from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer


# =========================
# REGISTER USER (PUBLIC)
# =========================
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User created successfully"
        }, status=201)

    return Response(serializer.errors, status=400)


# =========================
# CURRENT LOGGED-IN USER
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email
    })


# =========================
# LIST ALL USERS (FOR ADMIN LATER)
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.all()

    data = [
        {
            "id": u.id,
            "username": u.username,
            "email": u.email
        }
        for u in users
    ]

    return Response(data)


# =========================
# UPDATE USER PROFILE
# =========================
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user

    username = request.data.get("username")
    email = request.data.get("email")

    if username:
        user.username = username

    if email:
        user.email = email

    user.save()

    return Response({
        "message": "User updated successfully"
    })