import os, sys
try:
    __import__("update").main()
except Exception as e:
    exit(str(e))
