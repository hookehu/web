#-*- coding:utf-8 -*-
import time

class SessionManager:
	def __init__(self):
		pass

	def default_expire_time(self):
		t = time.time() * 1000 + 5 * 60000
		return t

	def add_session(self, uid, ip, mac, timestamp = 0):
		s = Session()
		s.user_id = uid
		s.ip = ip
		s.mac = mac
		if timestamp == 0:
			timestamp = self.default_expire_time()
		s.expire_time = timestamp
		s.save()

	def update_session(self, session, timestamp = 0):
		if timestamp == 0:
			timestamp = self.default_expire_time()
		session.expire_time = timestamp
		session.save()

	def del_session(self, session):
		session.delete()