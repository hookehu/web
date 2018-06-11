#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time, hashlib

from base import BaseView
from ..models import User, Session

class RegisterView(BaseView):
	need_site_permission = False
	url = r"register$"

	def __init__(self, request, *args, **kwargs):
		BaseView.__init__(self, request, *args, **kwargs)
		pass

	def get(self, request, *args, **kwargs):
		rst = {}
		rst['title'] = 'register'
		resp = render(request, "register.html", rst)
		return resp

	def post(self, request, *args, **kwargs):
		name = request.POST.get('username')
		pwd1 = request.POST.get('password1')
		pwd2 = request.POST.get('password2')
		phone = request.POST.get('phone')
		ip = request.META['REMOTE_ADDR']
		mac = ""
		m = hashlib.md5()
		m.update(pwd1)
		pwdmd5 = m.hexdigest()
		t = time.time() * 1000
		u = User()
		u.name = name
		u.password = pwdmd5
		u.phone = phone
		u.state = 0
		u.last_login_time = t
		u.create_ip = ip
		u.last_login_ip = ip
		u.create_time = t
		u.save()

		expire = t + 5 * 60000
		s = Session()
		s.user_id = u.id
		s.ip = ip
		s.mac = mac
		s.expire_time = expire
		s.save()

		content = redirect('/userapp/welcome')
		content.set_cookie('sid', s.id.get_hex())
		return content
