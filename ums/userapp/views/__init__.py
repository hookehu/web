#-*- coding:utf-8 -*-
import os

views = {}
def init_pkg():
    #print os.path.dirname(__file__)
    files = os.listdir(os.path.dirname(__file__))
    for file in files:
        fns = file.split('.')
        if len(fns) < 2:
            continue
        if fns[1] != 'py':
            continue
        if fns[0] == '__init__':
            continue
        #__all__.append(fns[0])
        pkg_name = __name__ + "." + fns[0]
        print pkg_name
        m = __import__(pkg_name, fromlist=('*'))
        _ms = dir(m)
        for name in _ms:
            if "View" not in name:
                continue
            views[name] = getattr(m, name)

init_pkg()

def register_builtin_views(site):
    for k, v in views.items():
        if not hasattr(v, 'url'):
            continue
        url = getattr(v, 'url')
        site.register_view(url, v)
