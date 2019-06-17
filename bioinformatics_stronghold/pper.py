#!/usr/bin/env python3

import math

with open('/home/smiravet/sam_things/rosalind.info/bioinformatics_stronghold/files/rosalind_pper.txt', 'r') as fi:
    for line in fi:
        n, k = [int(i) for i in line.strip().split()]

print(math.factorial(n)/math.factorial(n-k) % 1000000)
