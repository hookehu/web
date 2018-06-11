#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseView
from ..models import User, Session, Group, Sys, SysLimit
from .. import config

class SysLimitView(BaseView):
	need_site_permission = True
	url = r"sys_limit_mgr$"
	group_type = config.LimitGroupType.TYPE_SYS_LIMIT
	limit_name = "子系统权限列表"

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
