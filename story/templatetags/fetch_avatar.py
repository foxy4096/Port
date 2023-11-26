import hashlib
from django import template

register = template.Library()


@register.filter(name="fetch_avatar", is_safe=True)
def fetch_avatar(email):
    """
    Returns the avatar from the email.
    """
    return f"http://www.gravatar.com/avatar/{hashlib.md5(email.lower().encode()).hexdigest()}?s=50"
