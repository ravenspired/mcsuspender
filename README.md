# mcsuspender
A script to help reduce the performance impact of minecraft whenever it isn't being played.





Intended to be used for java Minecraft on macOS. 
Test bench: MacBook Pro 13" 2020 M1 running macOS Monterey 12.1, Minecraft 1.18.1 using MultiMC.

This program will work for any processes called "java", so any version of minecraft, modded or not, should work.




Installation Instructions:
Download the repo, extract it somewhere, open Terminal and type in ~/path/to/main.py (replacing the PATH as necessary.)

Dependencies:
pyConsole (bundled)
Apples' AppKit (included in standard Python Installation
Python 3 (2 will not work)


How it works: 
The program suspends the Minecraft process while it is not being used, saving battery and CPU power.
Using AppKit the program checks what window is in focus. If it is the java process, and the java process is unsuspended if it wasn't already. If it isn't the java process, it suspends java until focus is brought back. 
