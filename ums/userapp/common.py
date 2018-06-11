#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def error(request, err_msg):
	rst = {}
	rst['title'] = "出错啦"
	rst['user'] = request.user
	rst['reason'] = err_msg
	return render(request, "error.html", rst)

def check_name(name):
	return True

def check_phone(phone):
	return True

def check_mail(mail):
	return True

def check_num(num):
	return True

def check_url(url):
	return True
