from django import template
from django.utils.encoding import smart_str, force_unicode
from textwrap import dedent
from django.conf import settings

register = template.Library()


@register.tag(name="markdown")
def do_markdown(parser, token):
    nodelist = parser.parse(('endmarkdown',))
    parser.delete_first_token()
    return MarkdownNode(nodelist)


class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        try:
            import markdown
        except ImportError:
            if settings.DEBUG:
                raise template.TemplateSyntaxError("Error in {% markdown %} filter: The Python markdown library isn't installed.")
            return force_unicode(value)
        return markdown.markdown(dedent(output.strip()))


@register.tag(name="textile")
def do_textile(parser, token):
    nodelist = parser.parse(('endtextile',))
    parser.delete_first_token()
    return TextileNode(nodelist)


class TextileNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        try:
            import textile
        except ImportError:
            if settings.DEBUG:
                raise template.TemplateSyntaxError("Error in {% textile %} filter: The Python textile library isn't installed.")
        return force_unicode(value)
        return textile.textile(dedent(output.strip()))


@register.tag(name="restructuredtext")
def do_restructuredtext(parser, token):
    nodelist = parser.parse(('endrestructuredtext',))
    parser.delete_first_token()
    return RestructuredtextNode(nodelist)


class RestructuredtextNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
        try:
            from docutils.core import publish_parts
        except ImportError:
            if settings.DEBUG:
                raise template.TemplateSyntaxError("Error in {% restructuredtext %} filter: The Python docutils library isn't installed.")
            return force_unicode(value)
        parts = publish_parts(source=smart_str(dedent(output.strip())),
                              writer_name="html4css1",
                              settings_overrides=docutils_settings)
        return parts['whole']
