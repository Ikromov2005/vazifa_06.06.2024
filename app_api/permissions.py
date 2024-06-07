from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsOwnerOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return True
        # if request.method in SAFE_METHODS:
        #     return True
        #
        # if request.method == ['POST']:
        #     return request.user.is_superuser
        #
        # return False

    def has_object_permission(self, request, view, obj):
        return True
    


class IsOwnerOrReadOnly(permissions.BasePermission):
  
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user