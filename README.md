===========
django-markup-tags
===========

Django-markup-tags provides Markdown, Textile, and ReST template tags as
opposed to `filters <https://docs.djangoproject.com/en/dev/ref/contrib/markup/>'_.
Usage is simple, add ``'markuptags'`` to ``INSTALLED _APPS`` load it in the
template like so::


    {% load markuptags %}

    {% markdown %}
    A First Level Header
    ====================
    {% endmarkdown %}

    {% textile %}
    The EPA(Environmental Protection Agency) is measuring GHG(greenhouse gas) emissions.
    {% endtextile %}

    {% restructuredtext %}
    * a bullet point using "*"

      - a sub-list using "-"

        + yet another sub-list

      - another item
    {% endrestructuredtext %}

(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


A Section
=========

Lists look like this:

* First

* Second. Can be multiple lines
  but must be indented properly.

A Sub-Section
-------------

Numbered lists look like you'd expect:

1. hi there

2. must be going

Urls are http://like.this and links can be
written `like this <http://www.example.com/foo/bar>`_.


