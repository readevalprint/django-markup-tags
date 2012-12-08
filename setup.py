try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = "django-markup-tags",
    version = "0.1.2",
    packages = find_packages(),
    author = "Timothy Watts",
    author_email = "tim@readevalprint.com",
    description = "Template tags (not filters) for Markdown, Textile, and ReST.",
    url = "https://github.com/readevalprint/django-markup-tags",
    include_package_data = True
)