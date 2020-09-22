from django import template

register=template.Library()

def cut(value,arg):
    return value.replace(arg,' ')


register.filter('cutfilter',cut)
#cutfilter is the name that u use  to call in template tagging

#registering using decorators
@register.filter(name='splitfilter')
def cut(value):
    return value.split(' ')
