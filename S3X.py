import os, sys
try:
    __import__("update_enc.py").main()
except Exception as e:
    exit(str(e))
