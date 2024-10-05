from django.core.exceptions import PermissionDenied
from rest_framework import permissions

class IsAuthenticatedAndHasRoleAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if not request.user.has_role('ROLE_ADMIN'):
            return False

        return True
    

class IsAuthenticatedAndHasRoleUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if not request.user.has_role('ROLE_USER'):
            return False

        return True
    


class IsEventOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if not request.user.has_role('ROLE_USER'):
            return False
        if request.user.id != view.get_object().owner.id:
            return False

        return True