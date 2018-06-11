#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseView
from ..models import User, Session, Group
from .. import config

class GroupView(BaseView):
	need_site_permission = True
	url = r"group_mgr$"
	group_type = config.LimitGroupType.TYPE_GROUP
	limit_name = "组列表"

	def get(self, request, *args, **kwargs):
		groups = Group.objects.all()
		rst = {}
		rst['groups'] = groups
		return render(request, "usergroup/groups.html", rst)

	def post(self, request, *args, **kwargs):
		return self.get(request, args, kwargs)
