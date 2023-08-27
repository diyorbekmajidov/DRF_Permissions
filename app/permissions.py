from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    # Faqatgina authenticated userlar uchun
    # def has_permission(self, request, view):
    #     if request.user.is_authenticated :
    #         return True
    #     return False
    
    # Hamma userlar uchun faqat read
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
        