#-*- coding:utf-8 -*-
from django.conf.urls import url

class UserSite(object):
	def __init__(self):
		self.views = {}
		pass

	def register_view(self, path, view):
		self.views[path] = view
		pass

	def unregister_view(self, path, view):
		del self.views[path]
		pass

	@property
	def urls(self):
		urlpatterns = []
		for path, v in self.views.items():
			urlpatterns += [url(path, v.as_view())]
		return urlpatterns, '', ''

site = UserSite()
