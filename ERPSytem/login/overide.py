from rest_framework import permissions

class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """

    def has_permission(self, request, view):
        # import pdb;pdb.set_trace()
        if request.method=="GET" or request.method=="PUT" or request.method=="DELETE":
        
            return True
        # elif request.method =="PUT":
        #     return True
        
        return False
       
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        # import pdb;pdb.set_trace()
        if obj == request.user: 
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