#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def create_ele(d, q):
    for i in q:
        if d.get(i, 0) == 0:
            d[i] = [i, 1]

def find_root(d, find):
    root = find 
    while d.get(root)[0] != root:
        root = d.get(root)[0]
    return root

def solve_query(q, d, maxi):
    create_ele(d, q)
    q1 = find_root(d, q[0])
    q2 = find_root(d, q[1])
    
    if q1 == q2:
        return maxi
    
    if(d[q1][1] > d[q2][1]):
        d[q1][1] += d[q2][1]
        d[q2][0] = q1
        return max(maxi, d[q1][1])
    else:
        d[q2][1] += d[q1][1]
        d[q1][0] = q2
        return max(maxi, d[q2][1])
        
def maxCircle(queries):
    maxi = 1
    d = {}
    ar = []
    for q in queries:
        maxi = solve_query(q, d, maxi)
        ar.append(maxi)
    return ar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
