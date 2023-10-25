#!/bin/python3

import math
import os
import random
import re
import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                xor |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return xor

def maxXor(arr, queries):
    trie = Trie()
    result = []
    
    for num in arr:
        trie.insert(num)
    
    for query in queries:
        max_xor = trie.find_max_xor(query)
        result.append(max_xor)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
