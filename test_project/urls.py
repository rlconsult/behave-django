from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

import django

if django.VERSION < (1, 8):
    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        # Examples:
        # url(r'^$', 'test_project.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'^$', TemplateView.as_view(template_name='index.html')),

        url(r'^admin/', include(admin.site.urls)),
    )
else:
    urlpatterns = [
        # Examples:
        # url(r'^$', 'test_project.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'^$', TemplateView.as_view(template_name='index.html')),

        url(r'^admin/', include(admin.site.urls)),
    ]
