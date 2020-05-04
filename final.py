#!/usr/bin/python
#######################################################################
# Author: Nolen Young
# Date: 5-3-2020
# Desc: This program solves the LD problem.
#######################################################################

import math
import sys


def main(args):
    # unpack arguments into a tuple
    Q = ((int(args[0]), int(args[1]), int(args[2]), int(args[3])),
         (int(args[4]), int(args[5]), int(args[6]), int(args[7])))
    print("Equations: {}\n".format(Q))

    # find the FA's representing botch equations
    FAQ1 = constructFA(Q[0], 1)
    FAQ2 = constructFA(Q[1], 2)
    print("Finite Automata 1: {}".format(FAQ1))
    print("Finite Automata 2: {}\n".format(FAQ2))

    return 1


# this function will construct an FA based off the equations defined
# in the tuple Q.
def constructFA(eq, eqNum):
    FA = {} # stores final result graph, key: start node, value: edge, end node
    b = findB(eq[3]) # finds binary representation of C
    cMax = findCMax(eq) # finds cMax
    kc = findKC(eq[3]) # finds kc

    for carry in range(-cMax, cMax+1):
        for carryP in range(-cMax, cMax + 1):
            for i in range(1, findKC(eq[3] + 1)):
                for iP in range(1, findKC(eq[3] + 1)):
                    for a1 in range(2):
                        for a2 in range(2):
                            for a3 in range(2):
                                bi = b[i-1] # INDEX MIGHT BE WRONG *************************************************
                                R = (eq[0] * a1) + (eq[1] * a2) + (eq[2] * a3) + bi + carry
                                if (R % 2 == 0 and carryP == R / 2):
                                    if (i >= 1 and i <= kc):
                                        iP = i + 1
                                    else:
                                        iP = i
                                    FA[(carry, i)] = ((a1, a2, a3),(carryP, iP))

    return FA


# C: a tuple of 3 integers
# this function finds cMax, which is defined as:
# cMax = Max(abs(C1d1 + C2d2 + C3d3 + d)),
# where d and d1,2,3 are in the set {0, 1}
def findCMax(C):
    cMax = -1

    # loop through all combinations of d1, d2, d3, d,
    # where d is in the set {0,1}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
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
def findB(C):
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
