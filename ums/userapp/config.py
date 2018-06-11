#-*- coding:utf-8 -*-

USER_STATE_UNACTIVE = 0
USER_STATE_ACTIVE = 1
USER_STATE_DELETE = -1
SUPER_USER = 'admin'
SUPER_USER_PWD = '123456'

class LimitType:
	TYPE_URL = 0
	TYPE_MENU = 1
	TYPE_PAGE = 2
	TYPE_TAB = 3

class LimitGroupType:
	TYPE_WELCOME = 1
	TYPE_USER = 2
	TYPE_GROUP = 3
	TYPE_ROLE = 4
	TYPE_LIMIT = 5
	TYPE_SYS = 6
	TYPE_SYS_LIMIT = 7

	type_names = {
		TYPE_WELCOME:"欢迎",
		TYPE_USER:"用户管理",
		TYPE_GROUP:"组管理",
		TYPE_ROLE:"角色管理",
		TYPE_LIMIT:"权限管理",
		TYPE_SYS:"子系统管理",
		TYPE_SYS_LIMIT:"子系统权限",
	}
