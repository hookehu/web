#-*- coding:utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.
class User(models.Model):
	id = models.UUIDField(primary_key = True, default = uuid.uuid4)
	name = models.CharField(max_length = 256)
	password = models.CharField(max_length = 64)
	phone = models.CharField(max_length = 20)
	email = models.CharField(max_length = 128, default='')
	state = models.IntegerField()
	is_super_user = models.IntegerField(default = 0)
	last_login_time = models.BigIntegerField()
	create_time = models.BigIntegerField()
	create_ip = models.CharField(max_length = 20)
	last_login_ip = models.CharField(max_length = 20)
	class Meta:
		db_table = "core_user"

	def set_permission_mgr(self, mgr):
		self.permission = mgr
		mgr.init(self)

class UserRoleRelation(models.Model):
	id = models.AutoField(primary_key = True)
	user_id = models.UUIDField()
	role_id = models.IntegerField()
	class Meta:
		db_table = "core_user_role_relation"

class Group(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 32)
	parent_id = models.IntegerField(default = 0)
	class Meta:
		db_table = "core_group"

class UserGroupRelation(models.Model):
	id = models.AutoField(primary_key = True)
	user_id = models.UUIDField()
	group_id = models.IntegerField()
	class Meta:
		db_table = "core_user_group_relation"

class GroupRoleRelation(models.Model):
	id = models.AutoField(primary_key = True)
	group_id = models.IntegerField()
	role_id = models.IntegerField()
	class Meta:
		db_table = "core_group_role_relation"

class Role(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 128)
	class Meta:
		db_table = "core_role"

class RoleLimitRelation(models.Model):
	id = models.AutoField(primary_key = True)
	role_id = models.IntegerField()
	limit_id = models.IntegerField()
	class Meta:
		db_table = "core_role_limit_relation"

class RoleSysRelation(models.Model):
	id = models.AutoField(primary_key = True)
	role_id = models.IntegerField()
	sys_id = models.IntegerField();
	class Meta:
		db_table = "core_role_sys_relation"

class Limit(models.Model):
	id = models.AutoField(primary_key = True)
	type = models.IntegerField() #类型指定是url、菜单ID、页面ID、tab页、其它
	group_type = models.IntegerField() #分组类型相同为同一组
	group_name = models.CharField(max_length = 128, default = '')
	limit_name = models.CharField(max_length = 32)
	param = models.CharField(max_length = 256, default = '') #不同type对应不同内容
	class Meta:
		db_table = "core_limit"

class Session(models.Model):
	id = models.UUIDField(primary_key = True, default = uuid.uuid4)
	user_id = models.UUIDField(default = uuid.uuid4)
	expire_time = models.BigIntegerField()
	ip = models.CharField(max_length = 20)
	mac_address = models.CharField(max_length = 32, default = '')
	class Meta:
		db_table = "core_session"

class Token(models.Model):
	id = models.UUIDField(primary_key = True, default = uuid.uuid4)
	user_id = models.UUIDField(default = uuid.uuid4)
	expire_time = models.BigIntegerField()
	ip = models.CharField(max_length = 20)
	mac_address = models.CharField(max_length = 32, default = '')
	class Meta:
		db_table = "core_token"

class AuthCode(models.Model):
	id = models.UUIDField(primary_key = True, default = uuid.uuid4)
	user_id = models.UUIDField(default = uuid.uuid4)
	token_id = models.UUIDField(default = uuid.uuid4)
	expire_time = models.BigIntegerField()
	ip = models.CharField(max_length = 20)
	class Meta:
		db_table = "core_auth_code"

class OPLog(models.Model):
	id = models.BigAutoField(primary_key = True)
	user_id = models.UUIDField()
	method = models.CharField(max_length = 256)
	time = models.BigIntegerField()
	ip = models.CharField(max_length = 20)
	mac_address = models.CharField(max_length = 20, default = '')
	class Meta:
		db_table = "core_op_log"

class Sys(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 256)
	state = models.IntegerField()
	desc = models.TextField()
	redirect_url = models.CharField(max_length = 512, default='')
	class Meta:
		db_table = "core_sys"

class SysLimit(models.Model):
	id = models.AutoField(primary_key = True)
	limit = models.IntegerField()
	limit_name = models.CharField(max_length = 256)
	sys_id = models.IntegerField()
	class Meta:
		db_table = "core_sys_limit"

class UserSysLimitRelation(models.Model):
	id = models.AutoField(primary_key = True)
	user_id = models.IntegerField()
	sys_limit_id = models.IntegerField()
	class Meta:
		db_table = "core_user_sys_limit_relation"
