from django.template import Library


register = Library()

@register.tag
def escapejs(to_js_string):
    return to_js_string.replace('\n', '').replace('\'', "\\'")
