#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time, hashlib

from base import BaseView
from ..models import User, Session

class IndexView(BaseView):
	need_site_permission = False
	url = r"index$"

	def get(self, request, *args, **kwargs):
		rst = {}
		rst['title'] = '首页'
		return render(request, "index.html", rst)

	def post(self, request, *args, **kwargs):
		return self.get(request, args, kwargs)

class LogoutView(BaseView):
	need_site_permission = False
	url = r"logout$"

	def get(self, request, *args, **kwargs):
		sid = request.COOKIES.get('sid')
		s = Session.objects.get(id=sid)
		if s:
			s.delete()
		content = redirect('/userapp/index')
		content.set_cookie('sid', '')
		return content

	def post(self, request, *args, **kwargs):
		sid = request.COOKIES.get('sid')
		s = Session.objects.get(id=sid)
		if s:
			s.delete()
		content = redirect('/userapp/index')
		content.set_cookie('sid', '')
		return content

class LoginView(BaseView):
	need_site_permission = False
	url = r"login$"

	def get(self, request, *args, **kwargs):
		rst = {}
		rst['title'] = '登录'
		return render(request, "login.html", rst)

	def post(self, request, *args, **kwargs):
		name = request.POST.get('username')
		pwd = request.POST.get('password')
		u = User.objects.filter(name=name)
		u = u[0]
		ip = request.META['REMOTE_ADDR']
		mac = ""
		expire = time.time() * 1000 + 5 * 60000
		rst = {}
		m = hashlib.md5()
		m.update(pwd)
		pwdmd5 = m.hexdigest()
		if u.password == pwdmd5:
			s = Session(user_id=u.id, ip=ip, mac_address=mac, expire_time=expire)
			s.save()
			rst['sid'] = s.id.get_hex()
		content = redirect('/userapp/welcome')
		content.set_cookie('sid', s.id.get_hex())
		return content
