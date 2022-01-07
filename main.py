#!/usr/bin/python             



from console_resources import *                                                                                          
consoleSetup(True, True, True, True)




try:
    from AppKit import NSWorkspace
except ImportError:
    console("AppKit Import failed", "error")
    console("Try running with /usr/bin/python instead.", "info")
    exit(1)

from datetime import datetime
from time import sleep



import os



isPaused = False
print("1")
try:
	while True:
		active_app = NSWorkspace.sharedWorkspace().activeApplication()
		#console(active_app['NSApplicationName'], "info")
		if active_app['NSApplicationName'] == "java":
			
			if isPaused == True:
				print("\n")
				console("Process is paused and has been brought to focus.", "info")
				console("Attempting to continue process.", "info")
				os.system("killall -CONT java")
				console("Task succeeded.", "ok")
				isPaused = False

		else:
			if isPaused == False:
				print("\n")
				console("Minecraft is alive, not paused, and not focused.", "info")
				console("Attempting to pause process.", "info")
				os.system("killall -STOP java")
				console("Task succeeded.", "ok")
				isPaused = True
    
		#console("Waiting for something to change.", "info")
		sleep(1)
except KeyboardInterrupt:
	print("\n")
	console("Ctrl+C has been hit.", "warning")
	console("Attempting to resuscitate Minecraft Process...", "info")
	try:
		os.system("killall -CONT java")
	except:
		console("Resuscitation failed!", "error")
	
	console("Successfully resuscitated java.", "ok")
	console("Goodbye.", "info")

else:
	console("A fatal error has occured. Exiting.", "error")
