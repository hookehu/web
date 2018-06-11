#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UserappConfig(AppConfig):
	name = 'userapp'

	def ready(self):
		self.module.autodiscover()
		#setattr(xadmin,'site',xadmin.site)
