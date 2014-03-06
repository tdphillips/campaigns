from django.template import Library
from django.utils.safestring import mark_safe


register = Library()

@register.tag
def escapejs(to_js_string):
    return to_js_string.replace('\n', '').replace('\'', "\\'")


@register.filter
def make_help_text(help):
    html = '<div class="custom-help-block %s">%s</div>'

    return_html = ''

    for field, help_text in help.items():
        help_text_full = '<br>'.join(help_text)
        return_html += html % (field, help_text_full)

    return mark_safe(return_html)
