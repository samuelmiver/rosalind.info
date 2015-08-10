#!/usr/bin/env python

import os

def ins(a):
    """
    Given a positive integer m<= 10^3 and an array A[1..n] of integers
    Return the number of swaps performed by insertion sort algorithm of A[1..n]
    """

    ins = 0
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            a[k - 1], a[k] = a[k], a[k - 1]
            k = k - 1
            ins += 1
    return ins


if __name__ == "__main__":
    with open('./files/rosalind_ins.txt', 'r') as dataset:
        n = int(dataset.readline().strip())
        A = [int(r) for r in dataset.readline().strip().split()]

        print(ins(A))
