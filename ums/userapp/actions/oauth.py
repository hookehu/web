#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json, time

from base import BaseAction
from ..models import User, Session, Group, Sys, Token, AuthCode
from .. import config

class OAuthTokenAction(BaseAction):
	url = r"get_token$"

	def get(self, request, *args, **kwargs):
		code = request.GET.get('code', None)
		if not code:
			return
		auth = AuthCode.objects.get(id=code)
		if not auth:
			return
		token = Token.objects.get(id=auth.token_id)
		if not token:
			return
		pkg = {}
		pkg['tid'] = token.id.get_hex()
		json_str = json.dumps(pkg)
		return HttpResponse(json_str)

	def post(self, request, *args, **kwargs):
		code = request.POST.get('code', None)
		if not code:
			return
		auth = AuthCode.objects.get(id=code)
		if not auth:
			return
		token = Token.objects.get(id=auth.token_id)
		if not token:
			return
		pkg = {}
		pkg['tid'] = token.id.get_hex()
		json_str = json.dumps(pkg)
		return HttpResponse(json_str)

class OAuthResourceAction(BaseAction):
	url = r'get_resource$'

	def get(self, request, *args, **kwargs):
		token = request.GET.get('token', None)
		return	

	def post(self, request, *args, **kwargs):
		token = request.POST.get('token', None)
		if not token:
			return
		token = Token.objects.get(id=token)
		user = User.objects.get(id=token.user_id)
		pkg = {}
		pkg['openid'] = user.id.get_hex()
		pkg['name'] = user.name
		json_str = json.dumps(pkg).decode("raw_unicode_escape").encode('utf-8')
		return HttpResponse(json_str)
		pass

class OAuthCodeAction(BaseAction):
	url = r'auth$'

	def get(self, request, *args, **kwargs):
		sys_id = request.GET.get('sys', None)
		uid = request.GET.get('uid', None)

	def post(self, request, *args, **kwargs):
		pass
