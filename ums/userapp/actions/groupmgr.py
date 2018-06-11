#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseAction
from ..models import User, Session, Group, GroupRoleRelation, Role
from .. import config

class GroupAddAction(BaseAction):
	need_site_permission = True
	url = r"add_group$"
	group_type = config.LimitGroupType.TYPE_GROUP
	limit_name = "添加组"

	def get(self, request, *args, **kwargs):
		return render(request, "usergroup/group_add.html", {})

	def post(self, request, *args, **kwargs):
		user = request.user
		name = request.POST.get('name')
		pgid = request.POST.get('pgid')
		g = Group(name = name, parent_id = pgid)
		g.save()
		return render(request, "usergroup/group_add.html", {})


class GroupDelAction(BaseAction):
	need_site_permission = True
	url = r"del_group$"
	group_type = config.LimitGroupType.TYPE_GROUP
	limit_name = "删除组"

	def get(self, request, *args, **kwargs):
		gid = request.GET.get('gid')
		g = Group.objects.get(id=gid)
		print g
		if g:
			g.delete()
			#g.save()
		return redirect("/userapp/group_mgr")

	def post(self, request, *args, **kwargs):
		gid = request.POST.get('gid')
		g = Group.objects.get(id=gid)
		if g:
			g.delete()
		return redirect("/userapp/group_mgr")

class GroupModifyAction(BaseAction):
	need_site_permission = True
	url = r"modify_group$"
	group_type = config.LimitGroupType.TYPE_GROUP
	limit_name = "修改组"

	def get(self, request, *args, **kwargs):
		gid = request.GET.get('gid')
		g = Group.objects.get(id=gid)
		rst = {}
		rst['group'] = g
		return render(request, "usergroup/group_modify.html", rst)

	def post(self, request, *args, **kwargs):
		gid = request.POST.get('gid')
		name = request.POST.get('name')
		gpid = request.POST.get('pgid')
		g = Group.objects.get(id=gid)
		g.name = name
		g.parent_id = gpid
		g.save()
		rst = {}
		rst['group'] = g
		return render(request, "usergroup/group_modify.html", rst)

class GroupAssignRoleAction(BaseAction):
	need_site_permission = True
	url = r"assign_group_role$"
	group_type = config.LimitGroupType.TYPE_GROUP
	limit_name = "分配组角色"
	
	def get(self, request, *args, **kwargs):
		gid = request.GET.get('gid')
		group = Group.objects.get(id=gid)
		if not group:
			return
		relations = GroupRoleRelation.objects.filter(group_id=gid)
		hadroles = {}
		for r in relations:
			hadroles[r.role_id] = r.group_id
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "group_mgr"
		rst['user'] = request.user
		rst['group'] = group
		rst['roles'] = []
		for role in roles:
			r = {}
			r['id'] = role.id
			r['name'] = role.name
			if hadroles.has_key(role.id):
				r['check'] = 1
			else:
				r['check'] = 0
			rst['roles'].append(r)
		return render(request, "usergroup/group_role_relations.html", rst)

	def post(self, request, *args, **kwargs):
		gid = request.POST.get('gid')
		rids = request.POST.getlist('rids')
		rids = [int(i) for i in rids]
		group = Group.objects.get(id=gid)
		if not group:
			return
		relations = GroupRoleRelation.objects.filter(group_id=gid)
		hadroles = {}
		for r in relations:
			if r.role_id not in rids:
				r.delete()
				continue
			hadroles[r.role_id] = r.group_id
		for rid in rids:
			if hadroles.has_key(rid):
				continue
			else:
				newrelation = GroupRoleRelation()
				newrelation.group_id = gid
				newrelation.role_id = rid
				newrelation.save()
				hadroles[rid] = gid
		roles = Role.objects.all()
		rst = {}
		rst['title'] = "group_mgr"
		rst['user'] = request.user
		rst['group'] = group
		rst['roles'] = []
		for role in roles:
			r = {}
			r['id'] = role.id
			r['name'] = role.name
			if hadroles.has_key(role.id):
				r['check'] = 1
			else:
				r['check'] = 0
			rst['roles'].append(r)
		return render(request, "usergroup/group_role_relations.html", rst)
