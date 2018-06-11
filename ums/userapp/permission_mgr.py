#-*- coding:utf-8 -*-
from models import Group, Role, UserGroupRelation, GroupRoleRelation, RoleLimitRelation, Limit, RoleSysRelation, Sys

class PermissionManager:

	def __init__(self):
		pass

	def init(self, user):
		self.user = user
		ug_relations = UserGroupRelation.objects.filter(user_id = user.id)
		self.roles = []
		self.groups = []
		self.limits = []
		self.syss = []
		for ug in ug_relations:
			group = Group.objects.filter(id=ug.group_id)[0]
			self.groups.append(group)
			gr_relations = GroupRoleRelation.objects.filter(group_id = ug.group_id)
			for gr in gr_relations:
				role = Role.objects.filter(id = gr.role_id)[0]
				self.roles.append(role)
				rl_relations = RoleLimitRelation.objects.filter(role_id = gr.role_id)
				for rl in rl_relations:
					limit = Limit.objects.filter(id = rl.limit_id)[0]
					self.limits.append(limit)
				rs_relations = RoleSysRelation.objects.filter(role_id = gr.role_id)
				for rs in rs_relations:
					sys = Sys.objects.filter(id = rs.sys_id)[0]
					self.syss.append(sys)
		print self.roles, self.groups, self.limits, self.syss

	def has_permission(self, path):
		rst = False
		for limit in self.limits:
			if limit.param == path:
				rst = True
		if self.user.is_super_user == 1:
			rst = True
		return rst

	def is_superuser(self):
		return self.user.is_super_user == 1
