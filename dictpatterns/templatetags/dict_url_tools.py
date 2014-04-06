from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

import importlib

if settings.ROOT_DICTPATTERNS_NAME:
    UrlDictPatterns = getattr(importlib.import_module(settings.ROOT_URLCONF, settings.ROOT_DICTPATTERNS_NAME), settings.ROOT_DICTPATTERNS_NAME)
else:
    UrlDictPatterns = getattr(importlib.import_module(settings.ROOT_URLCONF, 'UrlDictPatterns'), "UrlDictPatterns")

register = template.Library()


@register.simple_tag(takes_context=True)
def this_url(context):
    return context["request"].path


@register.simple_tag(takes_context=True)
def parent_url(context, url=None):
    if not url:
        url = context["request"].path
    parent_url_dict = UrlDictPatterns.find_parent_url(url[1:])
    if parent_url_dict["name"]:
        return reverse(parent_url_dict["name"], args=parent_url_dict["args"])
    else:
        return ""
