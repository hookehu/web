#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseView
from ..models import User, Session, Group, Limit
from .. import config

class UserLimitView(BaseView):
	need_site_permission = True
	url = r"user_limit_mgr$"
	group_type = config.LimitGroupType.TYPE_LIMIT
	limit_name = "用户权限列表"

	def get(self, request, *args, **kwargs):
		limits = Limit.objects.all()
		rst = {}
		rst['title'] = "用户权限"
		rst['user'] = request.user
		rst['limits'] = limits
		inputs = []
		inputs.append({'desc':'权限类型int', 'type':'text', 'name':'type', 'value':''})
		inputs.append({'desc':'权限组类型int', 'type':'text', 'name':'group_type', 'value':''})
		inputs.append({'desc':'权限组名str', 'type':'text', 'name':'group_name', 'value':''})
		inputs.append({'desc':'权限名', 'type':'text', 'name':'limit_name', 'value':''})
		inputs.append({'desc':'权限参数', 'type':'text', 'name':'param', 'value':''})
		inputs.append({'desc':'Submit','type':'submit', 'name':'', 'value':'新增'})
		form = {'action':'''/userapp/add_user_limit''', 'method':'POST', 'inputs':inputs}
		rst['form'] = form
		return render(request, "user/user_limit.html", rst)

	def post(self, request, *args, **kwargs):
		return self.get(request, args, kwargs)
