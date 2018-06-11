#-*- coding:utf-8 -*-
from django.shortcuts import render
from base import BaseView

class ErrorView(BaseView):
	def get(self, request, *args, **kwargs):
		rst = {}
		rst['title'] = "error page"
		rst['user'] = user
		rst['reason'] = "error"
		return render(request, "error.html", rst)

	def post(self, request, *args, **kwargs):
		pass
