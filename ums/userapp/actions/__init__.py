#-*- coding:utf-8 -*-
import os

actions = {}
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
        m = __import__(pkg_name, fromlist=('*'))
        _ms = dir(m)
        for name in _ms:
            if "Action" not in name:
                continue
            actions[name] = getattr(m, name)
    #print actions

init_pkg()

def register_builtin_actions(site):
    for k, v in actions.items():
        if not hasattr(v, 'url'):
            continue
        url = getattr(v, 'url')
        site.register_view(url, v)
