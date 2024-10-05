# user_management/decorators.py
from django.http import HttpResponse
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                # Assuming `role` is the user field storing the role
                group = request.user.role

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page.")
            else:
                return HttpResponse("You need to login first.")
        return wrapper_func
    return decorator
