#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseAction
from ..models import User, Session, Group, Role, RoleLimitRelation, Limit, RoleSysRelation, Sys
from .. import config

class RoleAddAction(BaseAction):
	need_site_permission = True
	url = r"add_role$"
	group_type = config.LimitGroupType.TYPE_ROLE
	limit_name = "添加角色"

	def get(self, request, *args, **kwargs):
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		return render(request, "role/role_add.html", rst)

	def post(self, request, *args, **kwargs):
		name = request.POST.get('name')
		role = Role()
		role.name = name
		role.save()
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		return render(request, "role/role_add.html", rst)

class RoleDelAction(BaseAction):
	need_site_permission = True
	url = r"del_role$"
	group_type = config.LimitGroupType.TYPE_ROLE
	limit_name = "删除角色"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		role = Role.objects.get(id=id)
		if not role:
			return
		role.delete()
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['roles'] = roles
		return render(request, "role/roles.html", rst)

	def post(self, request, *args, **kwargs):
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['roles'] = roles
		return render(request, "role/roles.html", rst)

class RoleModifyAction(BaseAction):
	need_site_permission = True
	url = r"modify_role$"
	group_type = config.LimitGroupType.TYPE_ROLE
	limit_name = "修改角色"

	def get(self, request, *args, **kwargs):
		id = request.GET.get('id')
		role = Role.objects.get(id=id)
		role = Role.objects.get(id=id)
		if not role:
			return
		rst = {}
		rst['role'] = role
		return render(request, "role/role_modify.html", rst)

	def post(self, request, *args, **kwargs):
		id = request.POST.get('id')
		name = request.POST.get('name')
		role = Role.objects.get(id=id)
		role.name = name
		role.save()
		rst = {}
		rst['role'] = role
		return render(request, "role/role_modify.html", rst)

class RoleAssignLimitAction(BaseAction):
	need_site_permission = True
	url = r"assign_role_limit$"
	group_type = config.LimitGroupType.TYPE_ROLE
	limit_name = "分配角色权限"

	def get(self, request, *args, **kwargs):
		rid = request.GET.get('id')
		role = Role.objects.get(id=rid)
		if not role:
			return
		relations = RoleLimitRelation.objects.filter(role_id=rid)
		hadlimits = {}
		for r in relations:
			hadlimits[r.limit_id] = r.role_id
		limits = Limit.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['role'] = role
		limit_groups = {}
		limit_group = {}
		for limit in limits:
			limit_group = limit_groups.get(limit.group_type, None)
			if not limit_group:
				limit_group = {}
				limit_group['limits'] = []
				limit_groups[limit.group_type] = limit_group
			limit_group['group_name'] = limit.group_name
			l = {}
			l['id'] = limit.id
			l['name'] = limit.limit_name
			if hadlimits.has_key(limit.id):
				l['check'] = 1
			else:
				l['check'] = 0
			limit_group['limits'].append(l)
		rst['limit_groups'] = limit_groups.values
		return render(request, "role/role_limit_relations.html", rst)

	def post(self, request, *args, **kwargs):
		rid = request.POST.get('rid')
		ids = request.POST.getlist('lids')
		lids = [int(i) for i in ids]
		role = Role.objects.get(id=rid)
		if not role:
			return
		relations = RoleLimitRelation.objects.filter(role_id=rid)
		hadlimits = {}
		for r in relations:
			if r.limit_id not in lids:
				print 'del', r.limit_id
				r.delete()
				continue
			hadlimits[r.limit_id] = r.role_id
		for lid in lids:
			if hadlimits.has_key(lid):
				continue
			else:
				newrelation = RoleLimitRelation()
				newrelation.limit_id = lid
				newrelation.role_id = rid
				newrelation.save()
				hadlimits[lid] = rid
		limits = Limit.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['role'] = role
		limit_groups = {}
		limit_group = {}
		for limit in limits:
			limit_group = limit_groups.get(limit.group_type, None)
			if not limit_group:
				limit_group = {}
				limit_group['limits'] = []
				limit_groups[limit.group_type] = limit_group
			limit_group['group_name'] = limit.group_name
			l = {}
			l['id'] = limit.id
			l['name'] = limit.limit_name
			if hadlimits.has_key(limit.id):
				l['check'] = 1
			else:
				l['check'] = 0
			limit_group['limits'].append(l)
		rst['limit_groups'] = limit_groups.values
		return render(request, "role/role_limit_relations.html", rst)

class RoleAssignSysAction(BaseAction):
	need_site_permission = True
	url = r"assign_role_sys$"
	group_type = config.LimitGroupType.TYPE_ROLE
	limit_name = "分配角色系统"

	def get(self, request, *args, **kwargs):
		rid = request.GET.get('id')
		role = Role.objects.get(id=rid)
		if not role:
			return
		relations = RoleSysRelation.objects.filter(role_id=rid)
		hadsyss = {}
		for r in relations:
			hadsyss[r.sys_id] = r.role_id
		syss = Sys.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['role'] = role
		syslist = []
		for sys in syss:
			l = {}
			l['id'] = sys.id
			l['name'] = sys.name
			if hadsyss.has_key(sys.id):
				l['check'] = 1
			else:
				l['check'] = 0
			syslist.append(l)
		rst['syss'] = syslist
		return render(request, "role/role_sys_relations.html", rst)

	def post(self, request, *args, **kwargs):
		rid = request.POST.get('rid')
		ids = request.POST.getlist('sids')
		sids = [int(i) for i in ids]
		role = Role.objects.get(id=rid)
		if not role:
			return
		relations = RoleSysRelation.objects.filter(role_id=rid)
		hadsyss = {}
		for r in relations:
			if r.sys_id not in sids:
				print 'del', r.sys_id
				r.delete()
				continue
			hadsyss[r.sys_id] = r.role_id
		for sid in sids:
			if hadsyss.has_key(sid):
				continue
			else:
				newrelation = RoleSysRelation()
				newrelation.sys_id = sid
				newrelation.role_id = rid
				newrelation.save()
				hadsyss[sid] = rid
		syss = Sys.objects.all()
		rst = {}
		rst['title'] = "role_mgr"
		rst['user'] = request.user
		rst['role'] = role
		syslist = []
		for sys in syss:
			l = {}
			l['id'] = sys.id
			l['name'] = sys.name
			if hadsyss.has_key(sys.id):
				l['check'] = 1
			else:
				l['check'] = 0
			syslist.append(l)
		rst['syss'] = syslist
		return render(request, "role/role_sys_relations.html", rst)
