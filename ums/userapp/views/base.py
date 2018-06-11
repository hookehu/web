#-*- coding:utf-8 -*-
import functools
from functools import update_wrapper
from django.views.generic import View
from django.utils.decorators import method_decorator, classonlymethod

class BaseView(View):
	need_site_permission = False
	url = None

	def __init__(self, request, *args, **kwargs):
		View.__init__(self, **kwargs)
		self.request = request
		print request.method
		self.request_method = request.method.lower()
		self.init_request(*args, **kwargs)

	def init_request(self, *args, **kwargs):
		pass

	def get(self, request, *args, **kwargs):
		pass

	def post(self, request, *args, **kwargs):
		pass

	@classonlymethod
	def as_view(cls):
		def view(request, *args, **kwargs):
			self = cls(request, *args, **kwargs)

			if hasattr(self, 'get') and not hasattr(self, 'head'):
				self.head = self.get
			print self.request_method	
			if self.request_method == 'get':
				handler = self.get
			else:
				handler = self.post

			return handler(request, *args, **kwargs)

		# take name and docstring from class
		update_wrapper(view, cls, updated=())
		view.need_site_permission = cls.need_site_permission

		return view
