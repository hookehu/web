#-*- coding:utf-8 -*-

def get_param(request, key):
	if request.method == "GET":
		return request.GET.get(key, None)
	else:
		return request.POST.get(key, None)

