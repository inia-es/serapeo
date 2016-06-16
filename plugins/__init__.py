import os
import imp

_auth_path = 'plugins/auth'

def get_auth_plugins():
    plugin_files = [f[:-3] for f in os.listdir(_auth_path) if os.path.isfile(os.path.join(_auth_path, f)) and f.endswith('.py') and f != '__init__.py']

    plugin_tuples = map((lambda p: imp.find_module(p, [_auth_path])), [p for p in plugin_files])
    return map((lambda n, p: imp.load_module(n, p[0], p[1], p[2])), plugin_files, plugin_tuples)

def get_auth_plugin(p):
    plugin_tuple = imp.find_module(p, [_auth_path])
    return imp.load_module(p, plugin_tuple[0], plugin_tuple[1], plugin_tuple[2])

class Plugin(object):
    def __init__(self):
        self.name = 'No name'
        self.description = 'No description'

