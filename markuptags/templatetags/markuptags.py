from django import template
from django.utils.encoding import smart_str, force_unicode
import markdown, textile
from docutils.core import publish_parts
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
        return markdown.markdown(dedent(output))


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
        return textile.textile(dedent(output))


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
        parts = publish_parts(source=smart_str(dedent(output)), writer_name="html4css1", settings_overrides=docutils_settings)
        return parts['whole']
