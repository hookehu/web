#-*- coding:utf-8 -*-

class UserManager:
	def __init__(self):
		pass

	def add_user(self, name, pwd, phone, state, ip, timestamp):
		u = User()
		u.name = name
		u.password = pwd
		u.phone = phone
		u.state = state
		u.last_login_time = timestamp
		u.create_ip = ip
		u.last_login_ip = ip
		u.create_time = timestamp
		u.save()
		return True

	def update_user(self, user, **kwargs):
		for k, v in kwargs:
			user[k] = v
		user.save()
		return True

	def del_user(self, user):
		user.delete()
		return True
