print ("\x1b[32minjecting bypass File")
import os, sys
try:
    __import__("A")
except Exception as e:
    exit(str(e))
