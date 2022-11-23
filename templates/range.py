from django import template

register = template.Library()


@register.filter(name='_range')
def _range(start, end):
  return range(start, end)