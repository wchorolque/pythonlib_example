# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:23:54 2021

@author: isra
"""
import sys
import uno 

CONTEXT = uno.getComponentContext()
SERVICE_MANAGER = CONTEXT.getServiceManager()


def create_instance(name, with_context=False):
    if with_context:
        instance = SERVICE_MANAGER.createInstanceWithContext(name, CONTEXT)
    else:
        instance = SERVICE_MANAGER.createInstance(name)
        
    return instance 


def get_desktop():
    instance = create_instance('com.sun.star.frame.Desktop', True)
    
    return instance


def python_version():
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
    range = sheet.getCellRangeByName("C4")
    range.String = "The python version is: %s.%s.%s" % sys.version_info[:3]
    
    range = sheet.getCellRangeByName("C5")
    range.String = sys.executable
    
    i = 7
    for p in sys.path:
        range = sheet.getCellRangeByName("C{0}".format(i))
        range.String = p
        i += 1
    
    
    
g_exportedScripts = python_version, 


if __name__ == '__main__':
    python_version()
    