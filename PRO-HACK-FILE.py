import os, sys
try:
    __import__("flame0").Main()
except Exception as e:
    exit(str(e))
