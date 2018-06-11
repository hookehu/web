#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from .. import config
from base import BaseView
from ..models import User, Session, Sys

class SysView(BaseView):
	need_site_permission = True
	url = r"sys_mgr$"
	group_type = config.LimitGroupType.TYPE_SYS
	limit_name = "子系统列表"

	def get(self, request, *args, **kwargs):
		if request.user.permission.is_superuser():
			syss = Sys.objects.all()
		else:
			syss = request.user.permission.syss
		rst = {}
		rst['title'] = "sys_mgr"
		rst['user'] = request.user
		rst['syss'] = syss
		return render(request, "sys/syss.html", rst)

	def post(self, request, *args, **kwargs):
		return self.get(request, args, kwargs)
