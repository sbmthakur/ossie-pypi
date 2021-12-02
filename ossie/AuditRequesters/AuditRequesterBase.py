import requests
import json
from urllib import parse
import os

class AuditRequesterBase:
	def __init__(self, packages, user_creds_filepath, auth, creds):
		self.packages = packages  # list of tuples (name, version)
		self.user_creds_filepath = user_creds_filepath
		self.creds = creds
		self.auth = auth

	def perform_audit(self, audit_type, audit_name):
		print('    [+] Checking %d package(s)' % (len(self.packages)))
		audit_response = self.make_audit_request(audit_type, audit_name)
		if audit_response is None:
			if self.auth.env() == 'CICD':
				os.remove(self.user_creds_filepath)
			exit(1)
		else:
			self.audit_data = audit_response

	def make_audit_request(self, audit_type, audit_name):
		if not hasattr(self, 'package_manager'):
			raise Exception('package_manager attribute not set for AuditRequester')
		if not hasattr(self, 'packages'):
			raise Exception('packages attribute not set for AuditRequester')
		if not hasattr(self, 'creds'):
			raise Exception('creds attribute not set for AuditRequester')
		if not hasattr(self, 'auth'):
			raise Exception('auth attribute not set for AuditRequester')

		try:
			body = {
				"package_manager"	: self.package_manager,
				"request_type"		: audit_type,
				"request_name"		: audit_name,
				"packages"			: json.dumps(self.packages)
			}
			return self.auth.authorize_audit_request(body, self.creds)
		except Exception as e:
			print("Failed to audit: %s" % (str(e)))
			return None

