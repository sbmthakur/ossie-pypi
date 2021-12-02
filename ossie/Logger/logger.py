#!/usr/bin/python

import time
import logging
import os
import sys

###########################################################
# Logging
###########################################################
class Logger():
	__l = None

	def exception(self, msg):
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		self.__l.error("[%s, %s, %s] %s" % (exc_type, fname, exc_tb.tb_lineno, msg))

	def info(self, msg):
		self.__l.info(msg)

	def error(self, msg):
		self.__l.error(msg)

	def debug(self, msg):
		self.__l.debug(msg)

	def warning(self, msg):
		self.__l.warning(msg)

	def add_console(self):
		# also emit any warning/error/critical msgs to console
		console = logging.StreamHandler()
		console.setLevel(logging.WARNING)
		console.setFormatter(logging.Formatter('%(message)s'))
		self.__l.addHandler(console)

	def __init__(self, name, path=None, debug=False, \
					formatter='%(asctime)s, %(msecs)d, %(name)s, %(process)d, %(levelname)s, %(message)s'):
		try:
			self.__l = logging.getLogger(name)
			if debug:
				level=logging.DEBUG
			else:
				level=logging.INFO
			self.__l.setLevel(level)

			ts = time.strftime('%Y_%m_%d_%H_%M_%S')
			if path:
				handler = logging.FileHandler((path + '_' + str(os.getpid()) + '_' + ts + ".log"), mode='w')
			else:
				handler = logging.StreamHandler()
			handler.setFormatter(logging.Formatter(formatter))
			self.__l.addHandler(handler)

		except Exception as e:
			raise Exception("Error setting up %s logger: %s" % (name, str(e)))


if __name__ == "__main__":
	l = Logger("test") #, debug=True)
	l.debug("Hello")
