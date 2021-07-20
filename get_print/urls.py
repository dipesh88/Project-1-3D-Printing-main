from django.contrib import admin
from django.urls import path 
from get_print import views

appname = "get_print"

urlpatterns = [
    path("", views.home, name = 'home'),
    path("about", views.about, name = 'about'),
    path("register", views.register_request, name = 'register'),
    path("login", views.login_request, name = 'login'),
    path("logout", views.logout_request, name = 'logout'),
    path("workspace", views.workspace, name = 'workspace'),
    path("parts", views.parts, name='parts'),
    path("upload_part", views.upload_part, name='upload_part'), 
]
