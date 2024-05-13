from rest_framework.permissions import BasePermission


class IsActiveStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm():
            return True
        else:
            return False
