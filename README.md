django-markup-tags
==================

Django-markup-tags provides Markdown, Textile, and ReST template tags as
opposed to [filters](https://docs.djangoproject.com/en/dev/ref/contrib/markup/).
Usage is simple, add ``'markuptags'`` to ``INSTALLED _APPS`` load it in the
template like so:

    {% markdown %}
    A First Level Header
    ====================
    {% endmarkdown %}

    {% textile %}
    The EPA(Environmental Protection Agency) is measuring GHG(greenhouse gas) emissions.
    {% endtextile %}

    {% restructuredtext %}
    1) An enumerated list item

    2) Second item

       a) Sub item

             i) Sub-sub item

             3) Third item
    {% endrestructuredtext %}

INSTALLATION
------------
Install the stable version from pypi

`$ pip install django-markup-tags`

or live on the edge

`sudo pip install https://github.com/readevalprint/django-markup-tags/zipball/master`

It's that easy!


TODO
----
* tests


LICENSE
-------

Copyright (c) 2011, Timothy Watts tim@readevalprint.com

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
