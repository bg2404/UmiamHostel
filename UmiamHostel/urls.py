"""UmiamHostel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.views.generic import RedirectView
from django.urls import re_path, include
from umiam import urls
from . import settings

urlpatterns = [
    re_path('^$', RedirectView.as_view(pattern_name='umiam:index', permanent=False)),
    re_path('^admin/', admin.site.urls),
    re_path('^umiam/', include(urls), name='umiam'),
    re_path('^summernote/', include('django_summernote.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
