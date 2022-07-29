from rest_framework import permissions

# class IsAuthenticatedOrAdminOrReadOnly(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         is_admin = super().has_permission(request, view)
#         return request.method in permissions.SAFE_METHODS or is_admin


class IsOwnProfileOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj) :
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile ==  request.user.profile 