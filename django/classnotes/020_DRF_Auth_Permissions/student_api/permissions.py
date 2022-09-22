from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
     def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # get,head,option
            return True
        else:
            return bool(request.user and request.user.is_staff)


class IsAddedByUserorReadOnly(permissions.BasePermission):  
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff