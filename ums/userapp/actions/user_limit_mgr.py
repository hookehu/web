#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseAction
from ..models import User, Session, Group, Limit
from .. import config

class UserLimitAddAction(BaseAction):
	need_site_permission = True
	url = r"add_user_limit$"
	group_type = config.LimitGroupType.TYPE_LIMIT
	limit_name = "添加权限"

	def get(self, request, *args, **kwargs):
		rst = {}
		return render(request, "user/user_limit_add.html", rst)

	def post(self, request, *args, **kwargs):
		type = request.POST.get('type')
		group_type = request.POST.get('group_type')
		group_name = request.POST.get('group_name')
		limit_name = request.POST.get('limit_name')
		param = request.POST.get('param')
		limit = Limit()
		limit.type = type
		limit.group_type = group_type
		limit.group_name = group_name
		limit.limit_name = limit_name
		limit.param = param
		limit.save()
		rst = {}
		return render(request, "user/user_limit_add.html", rst)

class UserLimitDelAction(BaseAction):
	need_site_permission = True
	url = r"del_user_limit$"
	group_type = config.LimitGroupType.TYPE_LIMIT
	limit_name = "删除权限"

	def get(self, request, *args, **kwargs):
		lid = request.GET.get('lid')
		limit = Limit.objects.get(id=lid)
		limit.delete()
		limits = Limit.objects.all()
		rst = {}
		return render(request, "user/user_limit.html", rst)

	def post(self, request, *args, **kwargs):
		lid = request.POST.get('lid')
		limit = Limit.objects.get(id=lid)
		limit.delete()
		limits = Limit.objects.all()
		rst = {}
		return render(request, "user/user_limit.html", rst)

class UserLimitModifyAction(BaseAction):
	need_site_permission = True
	url = r"modify_user_limit$"
	group_type = config.LimitGroupType.TYPE_LIMIT
	limit_name = "修改权限"

	def get(self, request, *args, **kwargs):
		lid = request.GET.get('lid')
		limit = Limit.objects.get(id=lid)
		rst = {}
		rst['limit'] = limit
		return render(request, "user/user_limit_modify.html", rst)

	def post(self, request, *args, **kwargs):
		lid = request.POST.get('lid')
		type = request.POST.get('type')
		group_type = request.POST.get('group_type')
		group_name = request.POST.get('group_name')
		limit_name = request.POST.get('limit_name')
		param = request.POST.get('param')
		limit = Limit.objects.get(id=lid)
		limit.type = type
		limit.group_type = group_type
		limit.group_name = group_name
		limit.limit_name = limit_name
		limit.param = param
		limit.save()
		rst = {}
		rst['limit'] = limit
		return render(request, "user/user_limit_modify.html", rst)
