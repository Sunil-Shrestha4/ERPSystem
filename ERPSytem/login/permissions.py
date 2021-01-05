from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        import pdb; pdb.set_trace()
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

