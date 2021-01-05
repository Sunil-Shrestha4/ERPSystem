from rest_framework import permissions

class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """

    def has_permission(self, request, view):
        if request.method=="GET":
            return True
        return False
       
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        import pdb;pdb.set_trace()
        if obj == request.user: 
            return True
        else:
            return False