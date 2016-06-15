import plugins

def create_plugin():
    return LDAP()

class LDAP(plugins.Plugin):
    def __init__(self):
        self.name = 'LDAP'
