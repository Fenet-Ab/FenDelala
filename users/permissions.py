from rest_framework.permissions import BasePermission

class IsVerifiedConsultant(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        
        if not user.is_authenticated:
            return False
        
        # If not consultant, allow
        if user.role != "consultant":
            return True
        
        # If consultant, must be verified
        return hasattr(user, "consultant_profile") and user.consultant_profile.is_verified