from django import template
register = template.Library()

@register.filter(name='inearth')

def inearth(text):
    """return text witout spaces
    """
    return text.replace(' ', '_')
    
