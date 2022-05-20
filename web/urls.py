"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from froala_editor import views
from django.contrib.sitemaps.views import sitemap #this
from blog.sitemaps import PostSitemap #this
#this

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url
sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
     url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
 

  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('froala_editor/',include('froala_editor.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
