import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-markup-tags",
    version = "0.1.0",
    packages = find_packages(),
    author = "Timothy Watts",
    author_email = "tim@readevalprint.com",
    description = "Template tags (not filters) for Markdown, Textile, and ReST.",
    url = "https://github.com/readevalprint/django-markup-tags",
    include_package_data = True
)
