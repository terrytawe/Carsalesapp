from django import template
from authentication.utils import has_group, has_any_group

register = template.Library()

# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
@register.filter(name='has_group')
def has_group_filter(user, group_name):
    return has_group(user, group_name)


# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
@register.filter(name='has_any_group')
def has_any_group_filter(user, group_names):
    return has_any_group(user, group_names)