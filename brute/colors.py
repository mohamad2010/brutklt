"""
colors.py

    Describes application-wide constants that can be reused.
"""

# Color encodings
W = '\033[0m'       # white (normal)
R = '\033[31m'      # red
G = '\033[32m'      # green
O = '\033[33m'      # orange
B = '\033[34m'      # blue
P = '\033[35m'      # purple
C = '\033[36m'      # cyan
GR = '\033[37m'     # gray

def warn(input_str):
    print("{}{}{}".format(O, input_str, W))

def error(input_str):
    print("{}{}{}".format(R, input_str, W))

def good(input_str):
    print("{}{}{}".format(G, input_str, W))
