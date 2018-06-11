#-*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, time

from .. import config
from base import BaseView

class WelcomeView(BaseView):
	need_site_permission = True
	url = r"welcome$"
	default_limit = True
	group_type = config.LimitGroupType.TYPE_WELCOME
	limit_name = "欢迎界面"

	def get(self, request, *args, **kwargs):
		if not request.user:
			return redirect('/userapp/index')
		rst = {}
		rst['title'] = '用户中心'
		hrefs = []
		hrefs.append({'url':'/userapp/sys_mgr', 'name':u'子系统管理'})
		hrefs.append({'url':'/userapp/user_mgr', 'name':u'用户管理'})
		hrefs.append({'url':'/userapp/user_limit_mgr', 'name':u'用户权限管理'})
		hrefs.append({'url':'/userapp/sys_limit_mgr', 'name':u'子系统权限管理'})
		hrefs.append({'url':'/userapp/group_mgr', 'name':u'组织架构管理'})
		hrefs.append({'url':'/userapp/role_mgr', 'name':u'角色管理'})
		rst['hrefs'] = hrefs
		rst['user'] = request.user
		content = render(request, "welcome.html", rst)
		return content

	def post(self, request, *args, **kwargs):
		rst = {}
		rst['title'] = '用户中心'
		hrefs = []
		hrefs.append({'url':'/userapp/sys_mgr', 'name':u'子系统管理'})
		hrefs.append({'url':'/userapp/user_mgr', 'name':u'用户管理'})
		hrefs.append({'url':'/userapp/user_limit_mgr', 'name':u'用户权限管理'})
		hrefs.append({'url':'/userapp/sys_limit_mgr', 'name':u'子系统权限管理'})
		hrefs.append({'url':'/userapp/group_mgr', 'name':u'组织架构管理'})
		hrefs.append({'url':'/userapp/role_mgr', 'name':u'角色管理'})
		rst['hrefs'] = hrefs
		rst['user'] = request.user
		content = render(request, "welcome.html", rst)
		return content
