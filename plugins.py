import os

def get_auth_plugins():
    return [f for f in os.listdir('plugins/auth') if os.path.isdir(os.path.join('plugins/auth', f))]

# class Plugin(object):

