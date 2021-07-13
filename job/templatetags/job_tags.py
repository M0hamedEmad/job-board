from django import template

register = template.Library()

@register.filter
def mult(value, num):
    
    return (int(value)*int(num))

