from rest_framework import permissions

class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """

    def has_permission(self, request, view):
        # import pdb;pdb.set_trace()
        if request.method=="GET" or request.method=='POST':
        
            return True
        # elif request.method =="PUT":
        #     return True
        
        return False
       
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        # import pdb;pdb.set_trace()
        if obj == (request.user): 
            return True
        else:
            return False
class IsAbc(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """

    def has_permission(self, request, view):
        # import pdb;pdb.set_trace()
        if self.request.user.is_manager:
            


        
            return True
        # elif request.method =="PUT":
        #     return True
        
        return False

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to allow only owners of an object or administrators to access it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
        # if hasattr(obj, 'owner'):
        #     return obj.owner == request.user
        else:
            return False


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.owner == request.user
        else:
            return False
