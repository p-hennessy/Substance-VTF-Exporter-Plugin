##########################################################################
# ADOBE CONFIDENTIAL
# ___________________
#  Copyright 2010-2024 Adobe
#  All Rights Reserved.
# * NOTICE:  Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe,
# then your use, modification, or distribution of it requires the prior
# written permission of Adobe.
##########################################################################
 
import sd 
import logging
 
from vtf_exporter import menu

logger = logging.getLogger("VTF Exporter") 


def initializeSDPlugin():
    logger.addHandler(sd.getContext().createRuntimeLogHandler()) 
    logger.propagate = False 
    logger.setLevel(logging.DEBUG) 

    menu.create_menu()


def uninitializeSDPlugin(): 
    menu.destroy_menu()



