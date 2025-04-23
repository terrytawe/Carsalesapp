from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter
def has_any_group(user, group_names):
    return user.groups.filter(name__in=[g.strip() for g in group_names.split(',')]).exists()