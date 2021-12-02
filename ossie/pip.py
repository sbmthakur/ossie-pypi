#!/usr/bin/python3

import os
import sys

# Run the main entry point, similarly to how setuptools does it, but because
# we didn't install the actual entry point from setup.py, don't use the
# pkg_resources API.

def prompt_user():
	ret = None
	while ret not in ['Y', 'n']:
		print("Do you want to continue (Y/n)?", end=' ')
		ret = input()
	if ret == 'n':
		sys.exit(-1)

def audit_package(package):
	from .__main__ import main
	args = {
		'id'		: None,
		'all'		: None,
		'project'	: None,
		'package'	: package,
	}
	return main(mode='Audit', args=args)

def audit_project(project):
	from .__main__ import main
	print("<//> OssieBOT: auditing installation")
	args = {
		'id'		: None,
		'all'		: None,
		'project'	: project,
		'package'	: None,
	}
	return main(mode='Audit', args=args)

def audit_installation(args):
	try:
		packages = []
		for idx, arg in enumerate(args):
			if arg.startswith('-'):
				if arg == "-r":
					if os.path.isfile(args[idx+1]):
						if audit_project(os.getcwd()):
							prompt_user()
						return
					else:
						print("<//> OssieBOT: failed to gather requirements. Skipping audit.")
						return
				else:
					print("<//> OssieBOT: option %s not supported. Skipping audit." % (arg))
					return
			if arg == 'install':
				continue
			packages.append(arg)
		if not len(packages):
			print("<//> OssieBOT: failed to detect package name. Skipping audit.")
		else:
			print("<//> OssieBOT: auditing installation")
			for pkg in packages:
				if audit_package(pkg):
					prompt_user()
	except Exception as e:
		print("<//> OssieBOT: failed to audit package: %s" % (str(e)))

def main():
	if "install" in sys.argv:
		audit_installation(sys.argv[1:])
	import pip
	sys.exit(pip.main())

if __name__ == "__main__":
    main()
