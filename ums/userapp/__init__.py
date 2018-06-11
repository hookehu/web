#-*- coding:utf-8 -*-

from userapp.sites import site

def autodiscover():
	from userapp.views import register_builtin_views
	register_builtin_views(site)
	from userapp.actions import register_builtin_actions
	register_builtin_actions(site)

default_app_config = 'userapp.apps.UserappConfig'