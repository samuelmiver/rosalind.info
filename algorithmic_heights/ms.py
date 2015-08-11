#!/usr/bin/env python

def ins(unsorted):
    for i in range(1, len(unsorted)):
        k = i
        while k > 0 and unsorted[k] < unsorted[k-1]:
            t = unsorted[k]
            unsorted[k] = unsorted[k-1]
            unsorted[k-1] = t
            k -= 1
    return unsorted


def mer(arr1, arr2):
    n = len(arr1) + len(arr2)
    i1 = 0
    i2 = 0
    narr = list()

    for i in range(0, n):
        if i1 >= len(arr1) and i2 <= len(arr2):
            narr.append(arr2[i2])
            i2 += 1
        elif i1 <= len(arr1) and i2 >= len(arr2):
            narr.append(arr1[i1])
            i1 += 1
        elif arr1[i1] < arr2[i2]:
            narr.append(arr1[i1])
            i1 += 1
        else:
            narr.append(arr2[i2])
            i2 += 1

    return narr


def ms(unsorted_list):
    n = len(unsorted_list)
    n2 = int(round(n/2))
    if n > 5:
        m1 = ms(unsorted_list[0:n2])
        m2 = ms(unsorted_list[n2:n])
        return mer(m1, m2)
    else:
        return ins(unsorted_list)


unsorted = list()
f = open('files/rosalind_ms.txt', 'r')
for i, line in enumerate(f):
    if i == 1:
        arr = line.split(' ')
        for s in arr:
            unsorted.append(int(s))

sortedlist = ms(unsorted)

sortedlist = [str(x) for x in sortedlist]
print(' '.join(sortedlist))
