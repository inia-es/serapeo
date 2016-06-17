import ldap

NAME = 'serapeo_ldap'
DESCRIPTION = 'LDAP'

def validate(account, pwd, **kwargs):
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
