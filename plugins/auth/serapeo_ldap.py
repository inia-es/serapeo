"""Check valid users in a LDAP server"""
import ldap

NAME = 'serapeo_ldap'
DESCRIPTION = 'LDAP'

def validate(account, pwd, **kwargs):
    """Return account name for valid users in LDAP, or False elsewhere"""
    if not account.find('@'):
        account += '@inia.es'
    conn = ldap.initialize('ldap://server')
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    try:
        conn.simple_bind_s(account, pwd)
        conn.unbind()
        return account
    except ldap.INVALID_CREDENTIALS:
        return False
