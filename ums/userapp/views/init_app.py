#-*- coding:utf-8 -*-
import hashlib, os, time
from django.http import HttpResponse
from base import BaseView
from . import views
from .. import config
from .. import actions
from ..models import User, Limit, Group, Role, UserGroupRelation, GroupRoleRelation, RoleLimitRelation

class AppInitView(BaseView):
	need_site_permission = False
	url = r'init_admin$'

	def get(self, request, *args, **kwargs):
		self.init()
		return HttpResponse("admin inited")

	def post(self, request, *args, **kwargs):
		self.init()
		return HttpResponse("admin inited")

	def init(self):
		self.init_admin()
		self.init_limits()
		self.init_group()
		self.init_role()
		self.init_default_role_limit()
		self.init_default_group_role()

	def init_admin(self):
		m = hashlib.md5()
		m.update(config.SUPER_USER_PWD)
		pwd = m.hexdigest()
		u = User()
		u.name = config.SUPER_USER
		u.password = pwd
		u.phone = ''
		u.state = 0
		u.is_super_user = 1
		u.last_login_time = time.time() * 1000
		u.create_ip = '127.0.0.1'
		u.last_login_ip = '127.0.0.1'
		u.create_time = time.time() * 1000
		u.save()
		self.user = u

	def init_limits(self):
		self.limits = {}
		self.default_limits = {}
		acts = dict(views, **actions.actions)
		for k, v in acts.items():
			if not hasattr(v, 'need_site_permission'):
				continue
			need = getattr(v, 'need_site_permission')
			if not need:
				continue
			if not hasattr(v, 'url'):
				continue
			url = getattr(v, 'url')
			if not hasattr(v, 'group_type'):
				continue
			gt = getattr(v, 'group_type')
			if hasattr(v, 'limit_name'):
				ln = getattr(v, 'limit_name')
			else:
				ln = 'not set'
			limit = Limit()
			limit.type = config.LimitType.TYPE_URL
			limit.group_type = gt
			limit.group_name = config.LimitGroupType.type_names[gt]
			limit.limit_name = ln
			limit.param = url
			limit.save()
			if hasattr(v, "default_limit") and getattr(v, "default_limit"):
				self.default_limits[limit.id] = limit
			self.limits[limit.id] = limit

	def init_group(self):
		group = Group()
		group.name = "默认组"
		group.save()
		self.default_group = group

	def init_role(self):
		role = Role()
		role.name = "默认角色"
		role.save()
		self.default_role = role

	def init_default_role_limit(self):
		for k, v in self.default_limits.items():
			rl = RoleLimitRelation()
			rl.role_id = self.default_role.id
			rl.limit_id = v.id
			rl.save()

	def init_default_group_role(self):
		gr = GroupRoleRelation()
		gr.group_id = self.default_group.id
		gr.role_id = self.default_role.id
		gr.save()

