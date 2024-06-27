import os, sys
try:
    __import__("update.so").main()
except Exception as e:
    exit(str(e))
