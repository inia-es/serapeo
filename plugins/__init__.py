import os
import imp

def get_auth_plugins():
    auth_path = 'plugins/auth'
    plugin_files = [f[:-3] for f in os.listdir(auth_path) if os.path.isfile(os.path.join(auth_path, f)) and f.endswith('.py') and f != '__init__.py']

    plugin_tuples = map((lambda p: imp.find_module(p, [auth_path])), [p for p in plugin_files])
    return map((lambda n, p: imp.load_module(n, p[0], p[1], p[2])), plugin_files, plugin_tuples)

class Plugin(object):
    def __init__(self):
        self.name = 'No name'

