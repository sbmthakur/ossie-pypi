from .command_base import CommandBase
import subprocess
import re
import socket

class CheckAll(CommandBase):
	def __init__(self, auth, creds):
		super().__init__('all', 'system', auth, creds)

	def get_packages(self):
		pipreqs_command = ['pip', 'freeze']
		with open("/tmp/audit_req.txt", 'w') as tmpf:
			subprocess.run(pipreqs_command, stdout=tmpf)
		packages = self.get_packages_from_tmp_file()
		print("[+] Auditing all installed packages")
		return packages
