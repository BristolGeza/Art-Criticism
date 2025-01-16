# middleware.py
from django.core.exceptions import PermissionDenied

class CheckPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.has_perm('art.can_view_mymodel'):
            raise PermissionDenied
        response = self.get_response(request)
        return response
