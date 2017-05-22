"""Ultraman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from account import views as account_views
from project import views as project_views

urlpatterns = [
    url(r'^$', account_views.login, name='login'),
    url(r'logout', account_views.logout, name='logout'),
    url(r'checkuser', account_views.checkuser, name='checkuser'),
    url(r'registration', account_views.registration, name='registration'),
    url(r'register', account_views.register, name='register'),
    url(r'^project', project_views.project, name='project'),
    url(r'show_project_in_table', project_views.show_project_in_table, name='show_project_in_table'),
    url(r'ajax_opt_project', project_views.ajax_opt_project, name='ajax_opt_project'),
    url(r'ajax_del_project', project_views.ajax_del_project, name='ajax_del_project'),
    url(r'^project', project_views.project, name='project'),
    url(r'^admin/', admin.site.urls),
]
