from urllib.parse import urlparse

from django import template

register = template.Library()


@register.filter(name="parse_domain", is_safe=True)
def parse_domain(url):
    """
    Returns the domain of a URL.
    """
    return urlparse(url).netloc or None
