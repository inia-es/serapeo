import plugins.auth
import ldap 

def create_plugin():
    return LDAP()

class LDAP(plugins.auth.AuthPlugin):
    def __init__(self):
        self.name = 'serapeo_ldap'
        self.description = 'LDAP'

    def validate(self, *args):
        form = args[0]
        name = form['account']
        password = form['pwd']
        if not name.find('@'):
            name += '@inia.es'
        conn = ldap.initialize('ldap://server')
        conn.protocol_version = 3
        conn.set_option(ldap.OPT_REFERRALS, 0)
        try:
            conn.simple_bind_s(name, password)
            conn.unbind
            return name
        except Exception, error:
            return False 
