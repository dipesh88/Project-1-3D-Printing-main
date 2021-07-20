"""get_print URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.get_print, name='get_print')
Class-based views
    1. Add an import:  from other_app.views import get_print
    2. Add a URL to urlpatterns:  path('', get_print.as_view(), name='get_print')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_print/' , include('get_print.urls')),
]
