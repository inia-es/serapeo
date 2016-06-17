"""Get dynamic access to plugins"""
import os
import imp

_AUTH_PATH = 'plugins/auth'

def get_auth_plugins():
    """Return every plugin in the auth path"""
    plugin_files = [f[:-3] for f in os.listdir(_AUTH_PATH)
                    if os.path.isfile(os.path.join(_AUTH_PATH, f))
                    and f.endswith('.py') and f != '__init__.py'
                   ]
    plugin_tuples = [imp.find_module(p, [_AUTH_PATH]) for p in plugin_files]
    return [imp.load_module(n, p[0], p[1], p[2])
            for n in plugin_files for p in  plugin_tuples]

def get_auth_plugin(plugin_name):
    """Return an auth plugin given its name"""
    plugin_tuple = imp.find_module(plugin_name, [_AUTH_PATH])
    return imp.load_module(plugin_name, plugin_tuple[0], plugin_tuple[1], plugin_tuple[2])
