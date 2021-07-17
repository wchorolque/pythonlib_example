# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:31:33 2021

@author: isra
"""

from __future__ import unicode_literals

import uno
import os
import subprocess


def interpreter_console():
    ctx = XSCRIPTCONTEXT.getComponentContext()
    smgr = ctx.getServiceManager()
    ps = smgr.createInstanceWithContext("com.sun.star.util.PathSettings", ctx)
    install_path = uno.fileUrlToSystemPath(ps.Module)
    pgm = install_path + os.sep + "python"  # Python shell/console path
    subprocess.Popen(pgm)  # Start Python interactive Shell