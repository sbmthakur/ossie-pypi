#!/usr/bin/python

#################################################################
# Configuration parser
#################################################################
class Config():
	__configParser = None

	def __init__(self, file_path:str):
		try:
			import sys
			import os
			if not os.path.exists(file_path) or not os.path.isfile(file_path):
				raise Exception("Invalid config file %s" % (file_path))

			if sys.version_info[0] < 3:
				import ConfigParser
				self.__configParser = ConfigParser.RawConfigParser()
			else:
				import configparser
				self.__configParser = configparser.RawConfigParser(inline_comment_prefixes="#")
			self.__configParser.read(file_path)

		except ImportError as ie:
			raise Exception("configparser module not available. Please install")

		except Exception as e:
			raise Exception("Error parsing %s: %s" % (file_path, str(e)))

	def get(self, opt, sec="Main", typ=str):
		try:
			if typ == bool:
				return self.__configParser.getboolean(sec, opt)
			elif typ == int:
				return self.__configParser.getint(sec, opt)
			else:
				return self.__configParser.get(sec, opt)
		except Exception as e:
			raise Exception("Error getting config for section %s: %s" % (sec, str(e)))
