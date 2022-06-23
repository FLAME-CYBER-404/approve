print ("\x1b[32minjecting bypass File")
import os, sys
try:
    __import__("SpYPro").file()
except Exception as e:
    exit(str(e))
