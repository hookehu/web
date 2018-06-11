#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseView
from ..models import User, Session
from .. import config

class UsersView(BaseView):
	need_site_permission = True
	url = r"user_mgr$"
	group_type = config.LimitGroupType.TYPE_USER
	limit_name = "用户列表"

	def get(self, request, *args, **kwargs):
		rst = {}
		rst['title'] = "user_mgr"
		rst['user'] = request.user
		rst["users"] = []
		users = User.objects.all()
		for u in users:
			if u.state == config.USER_STATE_DELETE:
				continue
			rst['users'].append(u)
		content = render(request, "user/users.html", rst)
		return content

	def post(self, request, *args, **kwargs):
		return self.get(request, args, kwargs)
