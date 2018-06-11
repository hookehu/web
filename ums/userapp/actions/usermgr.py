#-*- coding:utf-8 -*-
import time
from django.shortcuts import render
from django.shortcuts import redirect
from base import BaseAction
from ..models import User, Group, UserGroupRelation
from .. import config

class UserAddAction(BaseAction):
	need_site_permission = True
	url = r"add_user$"
	group_type = config.LimitGroupType.TYPE_USER
	limit_name = "添加用户"

	def get(self, request, *args, **kwargs):
		resp = render(request, "user/user_add.html", {})
		return resp

	def post(self, request, *args, **kwargs):
		name = request.POST.get('username')
		pwd1 = request.POST.get('password1')
		pwd2 = request.POST.get('password2')
		phone = request.POST.get('phone')
		ip = request.META['REMOTE_ADDR']
		mac = ""
		t = time.time() * 1000
		u = User()
		u.name = name
		u.password = pwd1
		u.phone = phone
		u.state = 0
		u.last_login_time = t
		u.create_ip = ip
		u.last_login_ip = ip
		u.create_time = t
		u.save()
		return render(request, "user/user_add.html", {})
		
class UserDelAction(BaseAction):
	need_site_permission = True
	url = r"del_role$"
	group_type = config.LimitGroupType.TYPE_USER
	limit_name = "删除用户"

	def get(self, request, *args, **kwargs):
		uid = request.GET.get('uid')
		if not uid:
			return
		user = User.objects.get(id=uid)
		user.state = config.USER_STATE_DELETE
		user.save()
		return redirect('/userapp/user_mgr')
		pass

	def post(self, request, *args, **kwargs):
		pass

class UserModifyAction(BaseAction):
	need_site_permission = True
	url = r"modify_user$"
	group_type = config.LimitGroupType.TYPE_USER
	limit_name = "修改用户"

	def get(self, request, *args, **kwargs):
		uid = request.GET.get('uid')
		if not uid:
			return
		user = User.objects.get(id=uid)
		rst = {}
		rst['title'] = '修改用户信息'
		rst['user'] = user
		resp = render(request, "user/user_modify.html", rst)
		return resp

	def post(self, request, *args, **kwargs):
		name = request.POST.get('username')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		uid = request.POST.get('uid')
		user = User.objects.get(id=uid)
		if not user:
			return
		user.email = email
		user.phone = phone
		user.save()
		return redirect('/userapp/user_mgr')


class UserChangePwdAction(BaseAction):
	need_site_permission = True
	url = r"changepwd_user$"
	group_type = config.LimitGroupType.TYPE_USER
	limit_name = "修改用户密码"

	def get(self, request, *args, **kwargs):
		uid = request.GET.get('uid')
		if not uid:
			return
		user = User.objects.get(id=uid)
		rst = {}
		rst['user'] = user
		resp = render(request, "user/user_changepwd.html", rst)
		return resp

	def post(self, request, *args, **kwargs):
		uid = request.POST.get('uid')
		if not uid:
			return
		user = User.objects.get(id=uid)
		if not user:
			return
		oldpassword = request.POST.get('password')
		newpassword = request.POST.get('newpasswd')
		newpassword1 = request.POST.get('newpasswd1')
		if newpassword != newpassword1:
			return
		if oldpassword != user.password:
			return
		user.password = newpassword
		user.save()

		return redirect('/userapp/user_mgr')

class UserAssignGroupAction(BaseAction):
	need_site_permission = True
	url = r"assign_user_group$"
	group_type = config.LimitGroupType.TYPE_USER
	limit_name = "分配组用户"
	
	def get(self, request, *args, **kwargs):
		uid = request.GET.get('uid')
		user = User.objects.get(id=uid)
		if not user:
			return
		relations = UserGroupRelation.objects.filter(user_id=uid)
		hadgroups = {}
		for r in relations:
			hadgroups[r.group_id] = r.user_id
		groups = Group.objects.all()
		rst = {}
		rst['title'] = "user_mgr"
		rst['user'] = request.user
		rst['otheruser'] = user
		rst['groups'] = []
		for group in groups:
			r = {}
			r['id'] = group.id
			r['name'] = group.name
			if hadgroups.has_key(group.id):
				r['check'] = 1
			else:
				r['check'] = 0
			rst['groups'].append(r)
		return render(request, "user/user_group_relations.html", rst)

	def post(self, request, *args, **kwargs):
		uid = request.POST.get('uid')
		gids = request.POST.getlist('gids')
		gids = [int(i) for i in gids]
		user = User.objects.get(id=uid)
		if not user:
			return
		relations = UserGroupRelation.objects.filter(user_id=uid)
		hadgroups = {}
		for r in relations:
			if r.group_id not in gids:
				r.delete()
				continue
			hadgroups[r.group_id] = r.user_id
		for gid in gids:
			if hadgroups.has_key(gid):
				continue
			else:
				newrelation = UserGroupRelation()
				newrelation.group_id = gid
				newrelation.user_id = uid
				newrelation.save()
				hadgroups[gid] = uid
		groups = Group.objects.all()
		rst = {}
		rst['title'] = "user_mgr"
		rst['user'] = request.user
		rst['otheruser'] = user
		rst['groups'] = []
		for group in groups:
			r = {}
			r['id'] = group.id
			r['name'] = group.name
			if hadgroups.has_key(group.id):
				r['check'] = 1
			else:
				r['check'] = 0
			rst['groups'].append(r)
		return render(request, "user/user_group_relations.html", rst)
