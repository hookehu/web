#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from .. import config
from base import BaseView
from ..models import Role

class RoleView(BaseView):
	need_site_permission = True
	url = r"role_mgr$"
	group_type = config.LimitGroupType.TYPE_ROLE
	limit_name = "角色列表"

	def get(self, request, *args, **kwargs):
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['roles'] = roles
		return render(request, "role/roles.html", rst)

	def post(self, request, *args, **kwargs):
		return self.get(request, args, kwargs)
