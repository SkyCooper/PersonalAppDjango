from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
  
  # def has_permission(self, request, view):                --> view seviyesi
  # def has_object_permission(self, request, view, obj):    --> object seviyesi
  
  def has_object_permission(self, request, view, obj):
    return bool(request.user.is_staff or (obj.user == request.user))
  # or True aradığından 1 tanesi True olması yeterli
  



