#!/usr/bin/python
#######################################################################
# Author: Nolen Young
# Date: 5-3-2020
# Desc: This program solves the LD problem.
#######################################################################

import math
import sys


def main(args):
    Q = ((int(args[0]), int(args[1]), int(args[2]), int(args[3])),
         (int(args[4]), int(args[5]), int(args[6]), int(args[7])))
    print(Q)
    return 1


def constructFA():
    return 0


# C: a tuple of 3 integers
# this function finds cMax, which is defined as:
# cMax = Max(abs(C1d1 + C2d2 + C3d3 + d)),
# where d and d1,2,3 are in the set {0, 1}
def findCMax(C):
    cMax = -1

    # loop through all combinations of d1, d2, d3, d,
    # where d is in the set {0,1}
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                for l in range(0, 2):
                    temp = abs(int(C[0]) * i + int(C[1]) * j + int(C[2]) * k + l)  # calc score
                    if temp > cMax:  # if larger than max, set as max
                        cMax = temp

    return cMax


# this function returns the number of bits, Kc, to store a given
# constant, C, where C >= 0
def findKC(C):
    return math.ceil(math.log2(C + 1))


# this function returns bi, which represents all bits to represent
# a given constant, C, where C >= 0
def findBI(C):
    kc = findKC(C)
    bi = [0, ] * kc
    binary = str(bin(C))[2:]

    for i in range(kc):
        bi[i] = int(binary[i])

    return bi


# this block of code calls main if the script parameters are correct,
# and handles the exit code based off the results of main.
if __name__ == "__main__" and len(sys.argv[1:]) == 8:
    if main(tuple(sys.argv[1:])):
        print("Done")
        exit(0)
    else:
        print("Error: The program unexpectedly did not finish.")
        exit(1)
else:
    print("Error: Incorrect number arguments provided.")
    exit(1)
