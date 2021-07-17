# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:10:55 2021

@author: isra
"""
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
