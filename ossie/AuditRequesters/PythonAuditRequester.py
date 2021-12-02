from ..AuditRequesters.AuditRequesterBase import AuditRequesterBase

class PythonAuditRequester(AuditRequesterBase):
    def __init__(self, packages, user_creds_filepath, auth, creds):
        super().__init__(packages, user_creds_filepath, auth, creds)
        self.package_manager = "PyPi"
