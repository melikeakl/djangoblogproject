import bleach
from django import template

register = template.Library()

@register.filter
def clean_for_preview(value):
    allowed_tags = ['img', 'span', 'br', 'b', 'strong', 'del', 's', 'strike', 'i', 'em', 'u']  # Emoji için izin verilen etiketler
    allowed_attrs = {'img': ['src', 'alt'], 'span': ['class', 'style']}
    cleaned = bleach.clean(value, tags=allowed_tags, attributes=allowed_attrs, strip=True)
    return cleaned