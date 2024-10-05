from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
       Object-level permission to only allow owners of an object to edit it.
       Assumes the model instance has an `owner` attribute.
       """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.account == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.account == request.user
