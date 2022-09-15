from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.user == request.user


class IsStickerParentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.table.user == request.user


class IsTodoGrandParentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.sticker.table.user == request.user
