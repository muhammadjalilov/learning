from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "you are not the owner of this object"


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.account == request.user