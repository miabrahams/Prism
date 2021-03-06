# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2018 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.



import os, sys, traceback, time, subprocess
from functools import wraps

try:
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
except:
	from PySide.QtCore import *
	from PySide.QtGui import *


class Prism_PluginEmpty_Functions(object):
	def __init__(self, core, plugin):
		self.core = core
		self.plugin = plugin


	# this function catches any errors in this script and can be ignored
	def err_decorator(func):
		@wraps(func)
		def func_wrapper(*args, **kwargs):
			exc_info = sys.exc_info()
			try:
				return func(*args, **kwargs)
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				erStr = ("%s ERROR - Prism_Plugin_PluginEmpty %s:\n%s\n\n%s" % (time.strftime("%d/%m/%y %X"), args[0].plugin.version, ''.join(traceback.format_stack()), traceback.format_exc()))
				args[0].core.writeErrorLog(erStr)

		return func_wrapper


	# if returns true, the plugin will be loaded by Prism
	@err_decorator
	def isActive(self):
		return True


	# the following function are called by Prism at specific events, which are indicated by the function names
	# you can add your own code to any of these functions.
	@err_decorator
	def onProjectChanged(self, origin):
		pass


	@err_decorator
	def onProjectBrowserStartup(self, origin):
		pass


	@err_decorator
	def onProjectBrowserClose(self, origin):
		pass


	@err_decorator
	def onPrismSettingsOpen(self, origin):
		pass


	@err_decorator
	def onPrismSettingsSave(self, origin):
		pass


	@err_decorator
	def onStateManagerOpen(self, origin):
		pass


	@err_decorator
	def onStateManagerClose(self, origin):
		pass


	@err_decorator
	def onSelectTaskOpen(self, origin):
		pass


	@err_decorator
	def onStateCreated(self, origin):
		pass


	@err_decorator
	def onStateDeleted(self, origin):
		pass


	@err_decorator
	def onPublish(self, origin):
		pass


	@err_decorator
	def onSaveFile(self, origin, filepath):
		pass


	@err_decorator
	def onAssetDlgOpen(self, origin, assetDialog):
		pass


	@err_decorator
	def onAssetCreated(self, origin, assetName, assetPath, assetDialog=None):
		pass


	@err_decorator
	def onShotCreated(self, origin, sequenceName, shotName):
		pass


	@err_decorator
	def preLoadEmptyScene(self, origin):
		pass


	@err_decorator
	def postLoadEmptyScene(self, origin):
		pass


	@err_decorator
	def preImport(self, *args, **kwargs):
		pass


	@err_decorator
	def postImport(self, *args, **kwargs):
		pass


	@err_decorator
	def preExport(self, *args, **kwargs):
		pass


	@err_decorator
	def postExport(self, *args, **kwargs):
		pass


	@err_decorator
	def prePlayblast(self, *args, **kwargs):
		pass


	@err_decorator
	def postPlayblast(self, *args, **kwargs):
		pass


	@err_decorator
	def preRender(self, *args, **kwargs):
		pass


	@err_decorator
	def postRender(self, *args, **kwargs):
		pass