"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from . import views,search,search2
from blog import views as v2
from django.urls import re_path as url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^hello/", views.hello, name="hello"),
    url(r'^runoob/', views.runoob),
    url(r'^db_handle', v2.db_handle),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
    url(r'^post-user/$', v2.add_user),
    url(r'^query-user/$', v2.query_user),
]
