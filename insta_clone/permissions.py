from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsPublisherOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.user == request.user


class CanUpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated and obj == request.user) or request.user.is_superuser:
            return True
        return False
