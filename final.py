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
    print("Input Equations: {}\n".format(Q))

    # find the FA's representing botch equations
    M1 = constructFA(Q[0])
    M2 = constructFA(Q[1])
    # print("M1: {}".format(M1))
    # print("M2: {}\n".format(M2))

    # calculate the cartesian product of M1 x M2
    # this will give us our final graph
    M = computeCP(M1, M2)
    # print("M: {}\n".format(M))

    # Find a walk along M, if a walk exists, return yes, else no
    kc1 = findKC(Q[0][3])
    print(kc1)
    kc2 = findKC(Q[1][3])
    print(kc2)
    test = DFS(M, ((0, 1), (0, 1)), ((0, kc1+1), (0, kc2+1)))
    print("Path: {}".format(test))

    if test:
        print("Yes :D")
    else:
        print("No :(")

    return 1


# this function calls dfs helper to so do a dfs on M starting at init
# and ending at accepting. It will record the path the dfs takes as it goes
def DFS(M, init, accept):
    visited = set()
    path = ""
    print(accept)
    path = DFSHelper(visited, M, init, accept, path)

    print(path)
    return path


# recursively performs dfs on graph starting at node to accepting
# records path along the way
def DFSHelper(visited, graph, node, accept, path):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            newPath = "{}, {}".format(path, neighbour[0])
            print(neighbour[1])
            if neighbour[1] == accept:
                return newPath
            else:
                return DFSHelper(visited, graph, neighbour[1], accept, newPath)
    else:
        return ""


# this algorithm computes the cartesian product of two finite
# automata's, m1 and m2.
def computeCP(M1, M2):
    M = {} # our final solution

    # loop through each node in M1, then through edge in that node
    # then find all matching labeled edges in M2, and add that composite
    # edge to M
    for node1, edges1 in M1.items():
        for edge1 in edges1:
            for node2, edges2 in M2.items():
                for edge2 in edges2:
                    if edge1[0] == edge2[0]:
                        node = (node1, node2)
                        edge = (edge1[0], (edge1[1], edge2[1]))
                        if node in M.keys():
                            M[node].append(edge)
                        else:
                            M[node] = [edge]

    return M


# this function will construct an FA off the equations defined
# in the tuple Q.
def constructFA(eq):
    FA = {}  # stores final result graph, key: start node, value: edge, end node
    b = findB(eq[3])  # finds binary representation of C
    cMax = findCMax(eq)  # finds cMax
    kc = findKC(eq[3])  # finds kc

    # loop through every possible value of a variety of
    # variables, test each combo to see if it should be in
    # the graph
    for carry in range(-cMax, cMax + 1):
        for carryP in range(-cMax, cMax + 1):
            for i in range(1, kc + 2):
                for a1 in range(2):
                    for a2 in range(2):
                        for a3 in range(2):
                            bi = b[i - 2]  # INDEX MIGHT BE WRONG *************************************************
                            R = (eq[0] * a1) + (eq[1] * a2) + (eq[2] * a3) + bi + carry
                            if (R % 2 == 0 and carryP == R / 2):  # test if it is an edge in the FA
                                iP = i
                                if (i >= 1 and i <= kc):
                                    iP = iP + 1

                                if (carry, i) in FA.keys():
                                    FA[(carry, i)].append(((a1, a2, a3), (carryP, iP)))
                                else:
                                    FA[(carry, i)] = [((a1, a2, a3), (carryP, iP))]

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
    print("Error: Incorrect number arguments provided. Arguments should be in the form C11 C12 C13 C1 C21 C22 C23 C2")
    exit(1)
