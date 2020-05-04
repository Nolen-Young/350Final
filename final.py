#!/usr/bin/python

import sys

def main(args):
    cMax = CMax(args)
    return 1

def CMax(C):
    return 0


if __name__ == "__main__" and len(sys.argv) == 4:
    if main(tuple(sys.argv[1:])):
        print("Done")
        exit(0)
    else:
        print("Error: The program unexpectedly did not finish.")
        exit(1)
else:
    print("Error: Incorrect number arguments provided.")
    exit(1)
