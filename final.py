#!/usr/bin/python
#######################################################################
# Author: Nolen Young
# Date: 5-3-2020
# Desc: This program solves the LD problem.
#######################################################################

import sys

def main(args):
    cMax = CMax(args)
    print(cMax)
    return 1

# C: a tuple of 3 integers
# this function finds cMax, which is defined as:
# cMax = Max(abs(C1d1 + C2d2 + C3d3 + d)),
# where d and d1,2,3 are in the set {0, 1}
def CMax(C):
    max = -1

    # loop through all combinations of d1, d2, d3, d,
    # where d is in the set {0,1}
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                for l in range(0,2):
                    temp = abs(int(C[0]) * i + int(C[1]) * j + int(C[2]) * k + l) # calc score
                    if temp > max: # if larger than max, set as max
                        max = temp

    return max

# this block of code calls main if the script parameters are correct,
# and handles the exit code based off the results of main.
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
