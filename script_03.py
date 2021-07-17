# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:23:54 2021

@author: isra
"""
import sys
import uno

import session

from src.common import get_desktop

from src.operaciones.resta import restar
from src.operaciones.suma import sumar


def python_version_src():
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
    range = sheet.getCellRangeByName("C10")
    range.String = "The python version is: %s.%s.%s" % sys.version_info[:3]
    
    range = sheet.getCellRangeByName("C11")
    range.String = sys.executable
    
    i = 7
    for p in sys.path:
        range = sheet.getCellRangeByName("C{0}".format(i))
        range.String = p
        i += 1
    
    range = sheet.getCellRangeByName("A1")
    range.String = restar(8, 3)
    
    range = sheet.getCellRangeByName("B1")
    range.String = sumar(8, 3)
    
    return None
    
    
    
g_exportedScripts = python_version_src, 


if __name__ == '__main__':
    python_version_src()
    