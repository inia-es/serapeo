import plugins.auth
import ldap

def create_plugin():
    return LDAP()

class LDAP(plugins.auth.AuthPlugin):
    def __init__(self):
        self.name = 'serapeo_ldap'
        self.description = 'LDAP'

    def validate(self, account, pwd, **kwargs):
        if not account.find('@'):
            account += '@inia.es'
        conn = ldap.initialize('ldap://server')
        conn.protocol_version = 3
        conn.set_option(ldap.OPT_REFERRALS, 0)
        try:
            conn.simple_bind_s(account, pwd)
            conn.unbind()
            return account
        except Exception:
            return False
