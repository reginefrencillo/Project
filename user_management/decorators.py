from django.http import HttpResponse
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                group = request.user.role

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    # Return JavaScript code to trigger an alert popup
                    return HttpResponse('<script>alert("You are not authorized to view this page."); window.history.back();</script>')
            else:
                # Return JavaScript code to redirect to login with an alert popup
                return HttpResponse('<script>alert("You need to login first."); window.location.href="/login/";</script>')
        return wrapper_func
    return decorator
