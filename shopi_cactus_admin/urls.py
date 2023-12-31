"""
URL configuration for shopi_cactus_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from apps.users.api.views.register_apiview import create_client_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.routers')),
    path('plants/', include('apps.plants.api.routers')),
    path('orders/', include('apps.Order.api.routers')),
    path('create_order/', include('apps.Order.api.urls')),
    path('register/', create_client_api_view , name ='register')
]


urlpatterns+=[
    re_path(r'^media/(?P<path>.*)$',serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]