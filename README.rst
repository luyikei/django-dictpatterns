*******************
django-dictpatterns
*******************

In urls.py, you can write urlpatterns by using dictionary.

.. code-block:: python

    from django.conf.urls import include
    from django.contrib import admin
    admin.autodiscover()

    from dictpatterns.urls import DictPatterns

    UrlDictPatterns = DictPatterns(
        {
            r'^': ('testapp.views.home', 'home',
                {
                    r'test/': ('testapp.views.test', 'test',
                        {
                            r'(?P<id>\d*)/': ('testapp.views.test_n', 'test_n',
                                {
                                    r'd/': ('testapp.views.test_d', 'test_d')
                                }
                            )
                        }
                    ),
                    r'admin/': (include(admin.site.urls), 'admin')
                }
            )
        }
    )

    urlpatterns = UrlDictPatterns.to_patterns()

In template
===========

For the sake of this format, you can trace the parent url of a page.
You can display the parent url in template.

.. code-block:: html

    {% load dict_url_tools %}

    Now :
    <br>
    {% this_url %}
    <br>
    Parent :
    <br>
    {% parent_url %}

Settings
========

Make sure of writing DictPatterns in your urls which is distinguished as ROOT_URLCONF. 
And distinguish the root of DictPatterns as ROOT_DICTPATTERNS_NAME in settings.py if you need. Default value is "UrlDictPatterns".

