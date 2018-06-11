#-*- coding:utf-8 -*-
"""ums URL Configuration

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
#from django.contrib import admin
import views
import actions

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^index$', views.index),
    #url(r'^login$', views.login),
    #url(r'^login_act$', actions.login_act),
    #url(r'^register$', views.register),
    #url(r'^register_act$', actions.register_act),
    #url(r'^sys_mgr$', views.sys_mgr),
    #url(r'^user_mgr$', views.user_mgr),
    #url(r'^group_mgr$', views.group_mgr),
    #url(r'^user_limit_mgr$', views.user_limit_mgr),
    #url(r'^sys_limit_mgr$', views.sys_limit_mgr),
]
