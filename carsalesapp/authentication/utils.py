from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps

# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def group_required(groups, redirect_url='home'):
    # Decorator to restrict access to users in the given list of group names.
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return view_func(request, *args, **kwargs)
            messages.error(request, "You do not have permission to access this page.")
            return redirect(redirect_url)
        return _wrapped_view
    return decorator

# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def has_any_group(user, group_names):
    group_list = [g.strip() for g in group_names.split(',')]
    return user.groups.filter(name__in=group_list).exists()