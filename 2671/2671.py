from sys import stdin
import re

if re.match(r'^(100+1+|01)+$', stdin.readline().strip()):
    print("SUBMARINE")
else:
    print("NOISE")

