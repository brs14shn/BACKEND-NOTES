from rest_framework import permissions

# view bazında
class IsAdminorReadOnly(permissions.IsAdminUser):
    def has_permission(self,request,view):
        # GET
        if request.method in permissions.SAFE_METHODS:
            return True

        # POST,PUT,DELETE
        else:
            return bool(request.user.is_staff)

# object seviyesinde 
# objenin create edeni hangi user ise update ve delete yapma izni de ver

class IsAddedByUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff

