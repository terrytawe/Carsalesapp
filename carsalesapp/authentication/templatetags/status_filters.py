from django import template

register = template.Library()

@register.filter
def status_badge_class(value):
    return {
        'PENDING'       : 'warning',
        'IN_PROGRESS'   : 'warning', #'secondary'
        'COMPLETED'     : 'success',
        'CANCELLED'     : 'danger',
    }.get(value, 'light')

@register.filter
def is_pending(status):
    return status == 'PENDING'

@register.filter
def is_cancelled(status):
    return status == 'CANCELLED'

@register.filter
def is_active_status(status):
    return status in ['PENDING', 'IN_PROGRESS']