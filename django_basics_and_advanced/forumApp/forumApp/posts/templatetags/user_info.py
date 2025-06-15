from django import template

register = template.Library()


@register.inclusion_tag('common/user_info.html', takes_context=True)
def user_info(context):
    if context.request.user.is_authenticated:
        return {
            'username': context.request.user.username,
        }

    return {
            'username': 'Anonymous',
        }
