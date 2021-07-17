# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 19:47:19 2021

@author: isra
"""


import getpass
import os
import sys
import uno 
from pathlib import Path

class Session():
    @staticmethod
    def substitute(var_name):
        ctx = uno.getComponentContext()
        ps = ctx.getServiceManager().createInstanceWithContext(
            'com.sun.star.util.PathSubstitution', ctx)
    
        return ps.getSubstituteVariableValue(var_name)
    
    
    @staticmethod
    def Share():
        inst = uno.fileUrlToSystemPath(Session.substitute("$(prog)"))
        
        return os.path.normpath(inst.replace('program', "Share"))
    
    @staticmethod
    def SharedScripts():
        return ''.join([Session.Share(), os.sep, "Scripts"])
    
    @staticmethod
    def SharedPythonScripts():
        return ''.join([Session.SharedScripts(), os.sep, 'python'])
    
    @property
    def UserName(self):
        return getpass.getuser()
    
    @property
    def UserProfile(self):
        return uno.fileUrlToSystemPath(Session.substitute("$(user)"))
    
    @property
    def UserScripts(self):
        """return complete path to ~/LibreOffice/4/user/Scripts"""
        return ''.join([self.UserProfile, os.sep, 'Scripts'])
    
    @property
    def UserPythonScripts(self):
        """return complete path to ~/LibreOffice/4/user/Scripts/python"""
        return ''.join([self.UserScripts, os.sep, 'python'])
    
    

# Load ~/LibreOffice/4/user/Scripts in sys.path
user_lib = Session().UserPythonScripts
if not user_lib in sys.path:
    sys.path.insert(0, user_lib)
    
# Load package '' in sys.path
p = Path(__file__)
package_lib = str(p.parent.parent)
if not package_lib in sys.path:
    sys.path.insert(0, package_lib)
    
    