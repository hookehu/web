#-*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from utils import *
from models import Session, User
from permission_mgr import PermissionManager
import common

class SessionMiddleware(MiddlewareMixin):
	def process_request(self, request):
		sid = request.COOKIES.get("sid")
		if not sid:
			request.user = None
			return
		ss = Session.objects.filter(id=sid)
		if not ss or len(ss) == 0:
			print 'not session', sid
			request.user = None
			return
		s = ss[0]
		uid = s.user_id
		user = User.objects.get(id=uid)
		if not user:
			print 'not user', uid
			return
		user.set_permission_mgr(PermissionManager())
		request.user = user

	def process_response(self, request, response):
		return response

	def process_view(self, request, view_func, view_func_args, view_func_kwargs):
		pass

	def process_exception(self, request, exception):
		pass

	def process_template_response(self, request, response):
		return response

class PermissionMiddleware(MiddlewareMixin):
	def process_request(self, request):
		return

	def process_response(self, request, response):
		return response

	def process_view(self, request, view_func, view_func_args, view_func_kwargs):
		if not request.user:
			return None
		#not need permission
		if hasattr(view_func, "need_site_permission") and not getattr(view_func, "need_site_permission"):
			return None
		path = request.path[9:] + "$" #remove app prefix
		print path
		if request.user.permission.has_permission(path):
			return None
		return common.error(request, "权限不足")

	def process_exception(self, request, exception):
		pass

	def process_template_response(self, request, response):
		return response
