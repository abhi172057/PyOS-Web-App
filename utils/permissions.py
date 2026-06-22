from rest_framework.permissions import BasePermission, SAFE_METHODS


# =========================
# ADMIN ONLY
# =========================
class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, "profile") and
            request.user.profile.role == "ADMIN"
        )


# =========================
# USER OR ADMIN (GENERAL API ACCESS)
# =========================
class IsUserOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, "profile") and
            request.user.profile.role in ["USER", "ADMIN"]
        )


# =========================
# OBJECT LEVEL SECURITY (MAIN RULE)
# =========================
class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):

        # ADMIN can access everything
        if (
            request.user.is_authenticated and
            hasattr(request.user, "profile") and
            request.user.profile.role == "ADMIN"
        ):
            return True

        # OWNER ONLY
        return hasattr(obj, "owner") and obj.owner == request.user


# =========================
# READ ONLY OR OWNER (OPTIONAL FUTURE EXTENSION)
# =========================
class ReadOnlyOrOwner(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return (
            request.user.is_authenticated and
            hasattr(request.user, "profile")
        )

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return hasattr(obj, "owner") and obj.owner == request.user