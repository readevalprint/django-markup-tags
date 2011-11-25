from django import template
import markdown, textile
from docutils.core import publish_parts

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
        return markdown.markdown(output)


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
        return textile.textile(output)


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
        parts = publish_parts(source=output)
        return parts["fragment"]
