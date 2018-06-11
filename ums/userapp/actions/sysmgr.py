#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseAction
from ..models import User, Session, Group, Sys, Token, AuthCode
from .. import config

class SysAddAction(BaseAction):
	need_site_permission = True
	url = r"add_sys$"
	group_type = config.LimitGroupType.TYPE_SYS
	limit_name = "添加子系统"

	def get(self, request, *args, **kwargs):
		if request.user.permission.is_superuser():
			syss = Sys.objects.all()
		else:
			syss = request.user.permission.syss
		rst = {}
		return render(request, "sys/sys_add.html", rst)

	def post(self, request, *args, **kwargs):
		name = request.POST.get('name')
		state = request.POST.get('state')
		desc = request.POST.get('desc')
		url = request.POST.get('url')
		sys = Sys()
		sys.name = name
		sys.state = state
		sys.desc = desc
		sys.redirect_url = url
		sys.save()
		rst = {}
		return render(request, "sys/sys_add.html", rst)

class SysDelAction(BaseAction):
	need_site_permission = True
	url = r"del_sys$"
	group_type = config.LimitGroupType.TYPE_SYS
	limit_name = "删除子系统"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		sys = Sys.objects.get(id=id)
		if not sys:
			return
		sys.delete()
		syss = Sys.objects.all()
		rst = {}
		rst['syss'] = syss
		return render(request, "sys/syss.html", rst)

	def post(self, request, *args, **kwargs):
		syss = Sys.objects.all()
		rst = {}
		rst['syss'] = syss
		return render(request, "sys/syss.html", rst)

class SysModifyAction(BaseAction):
	need_site_permission = True
	url = r"modify_sys$"
	group_type = config.LimitGroupType.TYPE_SYS
	limit_name = "修改子系统"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		sys = Sys.objects.get(id=id)
		if not sys:
			return
		rst = {}
		rst['sys'] = sys
		return render(request, "sys/sys_modify.html", rst)

	def post(self, request, *args, **kwargs):
		id = request.POST.get('id')
		name = request.POST.get('name')
		state = request.POST.get('state')
		desc = request.POST.get('desc')
		url = request.POST.get('url')
		sys = Sys.objects.get(id=id)
		sys.name = name
		sys.state = state
		sys.desc = desc
		sys.redirect_url = url
		sys.save()
		rst = {}
		rst['sys'] = sys
		return render(request, "sys/sys_modify.html", rst)

class SysEnterAction(BaseAction):
	need_site_permission = True
	url = r'enter_sys$'
	greoup_type = config.LimitGroupType.TYPE_SYS
	limit_name = "进入子系统"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		sys = Sys.objects.get(id=id)
		if not sys:
			return

		token = Token()
		token.user_id = request.user.id
		token.ip = request.META['REMOTE_ADDR']
		token.expire_time = time.time() * 1000 + 5 * 60000
		token.save()
		code = AuthCode()
		code.user_id = request.user.id
		code.token_id = token.id
		code.expire_time = time.time() * 1000 + 5 * 1000
		code.ip = request.META['REMOTE_ADDR']
		code.save()
		rst = {}
		rst['title'] = sys.name
		rst['frame_url'] = sys.redirect_url + '?code=' + code.id.get_hex()
		rst['user'] = request.user
		# content = redirect('/userapp/index')
		# content.set_cookie('sid', '')
		# return content
		return render(request, "sys/sys_page.html", rst)
