import plugins

class AuthPlugin(plugins.Plugin):
    def validate(self, *args):
        raise NotImplementedError("""AuthPlugin cannot validate users.
            Extend it to access a specific auth system, or use a specific 
            module like `plugins.auth.ldap`""")
