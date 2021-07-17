# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:23:54 2021

@author: isra
"""
from __future__ import unicode_literals
import sys
import session

from myfuncion import myfuncion_saludar
from src.common import get_desktop

def python_version_pythonpath():
    desktop = get_desktop()
    model = desktop.getCurrentComponent()
    if not hasattr(model, "Sheets"):
        model = desktop.loadComponentFromURL(
            "private:factory/scalc", 
            "_blank",
            0, 
            ()
        )
        
    sheet = model.Sheets.getByIndex(0)
    range = sheet.getCellRangeByName("H4")
    range.String = "The python version is: %s.%s.%s" % sys.version_info[:3]
    
    range = sheet.getCellRangeByName("H5")
    range.String = sys.executable
    
    range = sheet.getCellRangeByName("H6")
    range.String = str(myfuncion_saludar())
    
    return None
    
    
    
g_exportedScripts = python_version_pythonpath, 


if __name__ == '__main__':
    python_version_pythonpath()
    