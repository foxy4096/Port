from django import template
from ..models import Story
register = template.Library()

@register.inclusion_tag("story/islands/story.html")
def story_block(story_id):
    return {"story": Story.objects.get(id=story_id)}