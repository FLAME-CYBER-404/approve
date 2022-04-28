import os, sys
try:
    __import__("paid").bnsbuy()
except Exception as e:
    exit(str(e))