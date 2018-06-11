#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseAction
from ..models import User, Session, Group, Sys, SysLimit
from .. import config

class SysLimitAddAction(BaseAction):
	need_site_permission = True
	url = r"add_sys_limit$"
	group_type = config.LimitGroupType.TYPE_SYS_LIMIT
	limit_name = "添加子系统权限"

	def get(self, request, *args, **kwargs):
		limits = SysLimit.objects.all()
		rst = {}
		rst['title'] = "系统权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'权限ID', 'type':'text', 'name':'limit', 'value':''})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'name', 'value':''})
		inputs.append({'desc':'所属子系统', 'type':'text', 'name':'sys', 'value':''})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'新增'})
		form = {'action':'''/userapp/add_sys_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "sys/sys_limit.html", rst)

	def post(self, request, *args, **kwargs):
		lid = request.POST.get('limit')
		name = request.POST.get('name')
		sys_id = request.POST.get('sys')
		limit = SysLimit()
		limit.limit = lid
		limit.limit_name = name
		limit.sys_id = sys_id
		limit.save()
		limits = SysLimit.objects.all()
		rst = {}
		rst['title'] = "系统权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'权限ID', 'type':'text', 'name':'limit', 'value':''})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'name', 'value':''})
		inputs.append({'desc':'所属子系统', 'type':'text', 'name':'sys', 'value':''})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'新增'})
		form = {'action':'''/userapp/add_sys_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "sys/sys_limit.html", rst)

class SysLimitDelAction(BaseAction):
	need_site_permission = True
	url = r"del_sys_limit$"
	group_type = config.LimitGroupType.TYPE_SYS_LIMIT
	limit_name = "删除子系统权限"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		limit = SysLimit.objects.get(id=id)
		if limit:
			limit.delete()
		limits = SysLimit.objects.all()
		rst = {}
		rst['title'] = "系统权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'权限ID', 'type':'text', 'name':'limit', 'value':''})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'name', 'value':''})
		inputs.append({'desc':'所属子系统', 'type':'text', 'name':'sys', 'value':''})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'新增'})
		form = {'action':'''/userapp/add_sys_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "sys/sys_limit.html", rst)

	def post(self, request, *args, **kwargs):
		limits = SysLimit.objects.all()
		rst = {}
		rst['title'] = "系统权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'权限ID', 'type':'text', 'name':'limit', 'value':''})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'name', 'value':''})
		inputs.append({'desc':'所属子系统', 'type':'text', 'name':'sys', 'value':''})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'新增'})
		form = {'action':'''/userapp/add_sys_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "sys/sys_limit.html", rst)

class SysLimitModifyAction(BaseAction):
	need_site_permission = True
	url = r"modify_sys_limit$"
	group_type = config.LimitGroupType.TYPE_SYS_LIMIT
	limit_name = "修改子系统权限"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		limit = SysLimit.objects.get(id=id)
		if not limit:
			return
		limits = SysLimit.objects.all()
		rst = {}
		rst['title'] = "系统权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'', 'type':'hidden', 'name':'id', 'value':limit.id})
		inputs.append({'desc':'权限ID', 'type':'text', 'name':'limit', 'value':limit.limit})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'name', 'value':limit.limit_name})
		inputs.append({'desc':'所属子系统', 'type':'text', 'name':'sys', 'value':limit.sys_id})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'保存'})
		form = {'action':'''/userapp/modify_sys_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "sys/sys_limit.html", rst)

	def post(self, request, *args, **kwargs):
		id = request.POST.get('id')
		lid = request.POST.get('limit')
		name = request.POST.get('name')
		sys_id = request.POST.get('sys')
		limit = SysLimit.objects.get(id=id)
		if not limit:
			return
		limit.limit = lid
		limit.limit_name = name
		limit.sys_id = sys_id
		limit.save()
		limits = SysLimit.objects.all()
		rst = {}
		rst['title'] = "系统权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'权限ID', 'type':'text', 'name':'limit', 'value':''})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'name', 'value':''})
		inputs.append({'desc':'所属子系统', 'type':'text', 'name':'sys', 'value':''})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'新增'})
		form = {'action':'''/userapp/add_sys_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "sys/sys_limit.html", rst)
